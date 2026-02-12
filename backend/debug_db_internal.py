import sys
import os
from datetime import datetime
# Force unbuffered output
sys.stdout.reconfigure(line_buffering=True)
print("DEBUG SCRIPT STARTED")

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# Use local file in current dir
SQLALCHEMY_DATABASE_URL = "sqlite:///./test_debug.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Define model inline to avoid import issues
from sqlalchemy import Column, String, Text, DateTime, Float, ForeignKey, JSON
from app.schemas.fir import FIRStatus

class Case(Base):
    __tablename__ = "cases"
    id = Column(String, primary_key=True)
    fir_number = Column(String, unique=True, index=True, nullable=False)
    status = Column(String, default=FIRStatus.DRAFT) 
    complaint_text = Column(Text, nullable=False)
    complainant_name = Column(String, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    # Minimal fields for test

def test_db():
    print("Creating tables...")
    try:
        Base.metadata.create_all(bind=engine)
        print("Tables created.")
    except Exception as e:
        print(f"Error creating tables: {e}")
        return

    print("Creating session...")
    db = SessionLocal()
    try:
        print("Creating case...")
        # Check if exists
        existing = db.query(Case).filter(Case.id == "test-id-123").first()
        if existing:
            print("Test case already exists.")
            db.delete(existing)
            db.commit()
            print("Deleted old test case.")

        case = Case(
            id="test-id-123",
            fir_number="FIR/TEST/001",
            status=FIRStatus.DRAFT, 
            complaint_text="Test complaint",
            complainant_name="Test User",
            created_at=datetime.now()
        )
        print("Adding to session...")
        db.add(case)
        print("Committing...")
        db.commit()
        print("Refreshing...")
        db.refresh(case)
        print(f"Success! Case ID: {case.id}")
    except Exception as e:
        print(f"Error: {e}")
        import traceback
        traceback.print_exc()
    finally:
        db.close()

if __name__ == "__main__":
    test_db()
