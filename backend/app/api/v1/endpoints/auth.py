
from fastapi import APIRouter, HTTPException, Depends
from pydantic import BaseModel
from typing import Optional
from sqlalchemy.orm import Session
from app.db.database import get_db, engine, Base
from app.models.user import User
from app.core.security import verify_password, get_password_hash, create_access_token

# Create tables if not exist (Simple migration)
Base.metadata.create_all(bind=engine)

router = APIRouter()

class UserCreate(BaseModel):
    email: str
    password: str
    role: str
    full_name: str
    # Optional fields
    station_id: Optional[str] = None
    court_id: Optional[str] = None
    department: Optional[str] = None
    badge_number: Optional[str] = None

class LoginRequest(BaseModel):
    email: str
    password: str

class GoogleLoginRequest(BaseModel):
    token: str

class AuthResponse(BaseModel):
    access_token: str
    token_type: str
    user_name: str
    user_email: str
    user_role: str
    avatar: Optional[str] = None

@router.post("/signup", response_model=AuthResponse)
def signup(user: UserCreate, db: Session = Depends(get_db)):
    print(f"DEBUG: Signup attempt for {user.email}")
    db_user = db.query(User).filter(User.email == user.email).first()
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    
    hashed_password = get_password_hash(user.password)
    new_user = User(
        email=user.email,
        hashed_password=hashed_password,
        role=user.role,
        full_name=user.full_name,
        station_id=user.station_id,
        court_id=user.court_id,
        department=user.department,
        badge_number=user.badge_number,
        avatar=f"https://api.dicebear.com/7.x/avataaars/svg?seed={user.full_name}"
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    
    access_token = create_access_token(data={"sub": new_user.email, "role": new_user.role, "id": new_user.id})
    return {
        "access_token": access_token,
        "token_type": "bearer",
        "user_name": new_user.full_name,
        "user_email": new_user.email,
        "user_role": new_user.role,
        "avatar": new_user.avatar
    }

@router.post("/login", response_model=AuthResponse)
def login(creds: LoginRequest, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.email == creds.email).first()
    if not user:
        # Fallback for demo users (admin/citizen/police/judge) if not in DB
        if creds.password == "password":
             access_token = create_access_token(data={"sub": creds.email, "role": "CITIZEN", "id": "demo"})
             return {
                "access_token": access_token,
                "token_type": "bearer",
                "user_name": "Demo User",
                "user_email": creds.email,
                "user_role": "CITIZEN", # Default fallback
                "avatar": ""
            }
        raise HTTPException(status_code=400, detail="Incorrect email or password")
        
    if not verify_password(creds.password, user.hashed_password):
        raise HTTPException(status_code=400, detail="Incorrect email or password")
        
    access_token = create_access_token(data={"sub": user.email, "role": user.role, "id": user.id})
    return {
        "access_token": access_token,
        "token_type": "bearer",
        "user_name": user.full_name,
        "user_email": user.email,
        "user_role": user.role,
        "avatar": user.avatar
    }

@router.post("/google", response_model=AuthResponse)
def google_login(payload: GoogleLoginRequest, db: Session = Depends(get_db)):
    # 1. Verify token with Google (Skipped for hackathon demo)
    # 2. Extract email from token
    email = "google-user@gmail.com" # Mock extraction
    name = "Google User"
    
    user = db.query(User).filter(User.email == email).first()
    if not user:
        # Auto-signup
        user = User(
            email=email,
            hashed_password=get_password_hash("google_auth"),
            role="CITIZEN",
            full_name=name,
            avatar="https://api.dicebear.com/7.x/avataaars/svg?seed=Google"
        )
        db.add(user)
        db.commit()
        db.refresh(user)
    
    access_token = create_access_token(data={"sub": user.email, "role": user.role, "id": user.id})
    return {
        "access_token": access_token,
        "token_type": "bearer",
        "user_name": user.full_name,
        "user_email": user.email,
        "user_role": user.role,
        "avatar": user.avatar
    }
