from pydantic_settings import BaseSettings
from typing import List

class Settings(BaseSettings):
    PROJECT_NAME: str = "LegalOS 4.0"
    VERSION: str = "4.0.0"
    DESCRIPTION: str = "AI-powered judicial case management system"
    
    # Security
    SECRET_KEY: str = "your-secret-key-change-in-production"
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    
    # CORS
    ALLOWED_ORIGINS: List[str] = [
        "http://localhost:5173",
        "http://localhost:3000",
        "http://127.0.0.1:5173",
        "http://127.0.0.1:3000",
        "http://localhost:5174",
        "http://127.0.0.1:5174"
    ]
    
    # Database
    DATABASE_URL: str = "sqlite:///./legalos.db"  # Changed to sqlite for easier setup without docker
    
    # Redis
    REDIS_URL: str = "redis://localhost:6379"
    
    # Judicial Settings
    MAX_DAILY_MINUTES: int = 330  # 5.5 hours
    LUNCH_BREAK_MINUTES: int = 60
    
    class Config:
        env_file = ".env"

settings = Settings()
