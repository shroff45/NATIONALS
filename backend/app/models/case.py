import uuid
from datetime import datetime
from sqlalchemy import Column, String, Text, DateTime, Float, ForeignKey, JSON, Enum # noqa: F401
from sqlalchemy.orm import relationship # noqa: F401
from app.db.database import Base
from app.schemas.fir import FIRStatus

class Case(Base):
    __tablename__ = "cases"

    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    fir_number = Column(String, unique=True, index=True, nullable=False)
    
    # Complainant Details
    complainant_id = Column(String, ForeignKey("users.id"), index=True, nullable=True) # Optional for now if anonymous. Index for Multi-tenant filtering and Row-Level Security
    complainant_name = Column(String, nullable=False)
    complainant_contact = Column(String, nullable=True)
    
    # Incident Details
    complaint_text = Column(Text, nullable=False)
    incident_location = Column(String, nullable=True)
    incident_datetime = Column(DateTime, nullable=True)
    
    # System Metadata
    status = Column(String, index=True, default=FIRStatus.DRAFT) # Enum stored as string. Index for Status-based filtering (e.g., active cases, draft cases)
    police_station_id = Column(String, index=True, nullable=True) # Index for Police Station specific filtering and assignments
    
    # AI Analysis (JSON)
    analysis_data = Column(JSON, nullable=True) # Stores analysis.json()
    confidence_score = Column(Float, default=0.0)
    
    # Meta
    created_at = Column(DateTime, index=True, default=datetime.utcnow) # Index for chronological sorting and date-range filtering in dashboards
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    # Relationships
    # complainant = relationship("User", back_populates="cases") 
