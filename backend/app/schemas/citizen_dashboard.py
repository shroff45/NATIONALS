from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime

class DashboardCase(BaseModel):
    id: str
    fir_number: str
    status: str
    description: str
    updated_at: datetime
    location: Optional[str] = None

class DashboardStats(BaseModel):
    active_cases: int
    pending_actions: int
    next_hearing: Optional[datetime] = None
    happiness_index: float

class Notification(BaseModel):
    id: str
    title: str
    message: str
    type: str # 'alert', 'info', 'success'
    timestamp: datetime

class WelfareService(BaseModel):
    id: str
    title: str
    description: str
    contact: str
    category: str

class CitizenDashboardResponse(BaseModel):
    user_name: str
    stats: DashboardStats
    recent_cases: List[DashboardCase]
    notifications: List[Notification]
    services: List[WelfareService]

class SOSRequest(BaseModel):
    location: str
    coordinates: Optional[str] = None
    type: str = "general" # 'medical', 'police', 'fire'

class SOSResponse(BaseModel):
    status: str
    message: str
    dispatch_id: str
