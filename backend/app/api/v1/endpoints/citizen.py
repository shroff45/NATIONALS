"""
Citizen Portal Backend Algorithm
Implements the core logic for NyayaSetu Dashboard, SOS, and Welfare services.
"""
from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from typing import List, Optional
from datetime import datetime, timedelta
import uuid

from app.db.database import get_db
from app.models.user import User
from app.models.case import Case
from app.dependencies import get_current_user # Allows all authenticated users
from app.schemas.citizen_dashboard import (
    CitizenDashboardResponse, DashboardStats, DashboardCase,
    Notification, WelfareService, SOSRequest, SOSResponse
)

router = APIRouter()

# Static Welfare Services Database
WELFARE_SERVICES = [
    WelfareService(id="ws-1", title="Women Safety SOS (Shakti)", description="Immediate assistance for women in distress. One-touch dial to 1091.", contact="1091", category="emergency"),
    WelfareService(id="ws-2", title="Child Protection", description="Reporting child abuse and missing children via 1098 helpline.", contact="1098", category="child_safety"),
    WelfareService(id="ws-3", title="Free Legal Aid", description="Apply for pro-bono legal counsel through NALSA/DLSA.", contact="15100", category="legal"),
    WelfareService(id="ws-4", title="Senior Citizen Support", description="Dedicated helpline for elderly citizens facing abuse or neglect.", contact="14567", category="senior_citizen"),
    WelfareService(id="ws-5", title="Victim Support Hub", description="Counseling and rehabilitation services for victims of crime.", contact="181", category="support"),
    WelfareService(id="ws-6", title="Cybercrime Report", description="Report online financial fraud and harassment instantly.", contact="1930", category="cyber"),
]

@router.get("/home", response_model=CitizenDashboardResponse)
async def get_dashboard(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """
    Get comprehensive citizen dashboard data (/citizen/home).
    Aggregates active cases, notifications, pending actions, and welfare services.
    """
    # 1. Fetch User Cases
    # Case.complainant_id is String (likely User ID as string or UUID)
    # User.id is Integer. We cast to string for query compatibility.
    user_id_str = str(current_user.id)

    # Query logic: Filter by complainant_id
    user_cases = db.query(Case).filter(Case.complainant_id == user_id_str).order_by(Case.updated_at.desc()).all()

    # 2. Calculate Stats
    active_cases = [c for c in user_cases if c.status not in ["CLOSED", "DISMISSED", "ACQUITTED"]]
    active_count = len(active_cases)

    # Mock 'Pending Actions' based on case status (e.g., if status is 'DRAFT')
    pending_actions = len([c for c in user_cases if c.status == "DRAFT"])

    # Mock Happiness Index (could come from Feedback service)
    happiness_index = 4.2 # Default if no feedback

    # 3. Transform Cases for Display
    recent_cases_response = []
    for c in user_cases[:5]: # Return top 5 recent
        desc = c.complaint_text[:80] + "..." if c.complaint_text else "No description available"
        recent_cases_response.append(
            DashboardCase(
                id=c.id,
                fir_number=c.fir_number,
                status=c.status,
                description=desc,
                updated_at=c.updated_at,
                location=c.incident_location
            )
        )

    # 4. Generate Notifications (Simulated Logic)
    # In a real system, query a Notification table.
    # Here, we generate notifications based on recent case updates.
    notifications = []
    for c in active_cases[:3]:
        days_since_update = (datetime.utcnow() - c.updated_at).days
        if days_since_update < 3:
            notifications.append(
                Notification(
                    id=str(uuid.uuid4()),
                    title="Case Update",
                    message=f"Status changed to {c.status} for FIR {c.fir_number}",
                    type="info",
                    timestamp=c.updated_at
                )
            )

    # Add generic welcome/onboarding if no notifications
    if not notifications:
        notifications.append(
            Notification(
                id=str(uuid.uuid4()),
                title="Welcome to NyayaSetu",
                message="Your legal assistant is ready. Try 'RightsAssistant' or 'File Complaint'.",
                type="success",
                timestamp=datetime.utcnow()
            )
        )

    # 5. Construct Response
    return CitizenDashboardResponse(
        user_name=current_user.full_name,
        stats=DashboardStats(
            active_cases=active_count,
            pending_actions=pending_actions,
            next_hearing=None, # Hearing dates not yet in Case model
            happiness_index=happiness_index
        ),
        recent_cases=recent_cases_response,
        notifications=notifications,
        services=WELFARE_SERVICES[:4] # Show top 4 services
    )


@router.post("/sos", response_model=SOSResponse)
async def trigger_sos(
    request: SOSRequest,
    current_user: User = Depends(get_current_user)
):
    """
    Trigger Emergency SOS.
    - Logs the request (Audit Trail).
    - Simulates dispatch to Police Control Room (100).
    - Can integrate with 'police.py' if needed.
    """
    dispatch_id = f"SOS-{uuid.uuid4().hex[:8].upper()}"
    timestamp = datetime.utcnow()

    # Log to console/audit
    print(f"🚨 EMERGENCY SOS TRIGGERED | User: {current_user.email} | Loc: {request.location} | LatLong: {request.coordinates} | ID: {dispatch_id}")

    # Simulation of dispatch logic
    return SOSResponse(
        status="dispatched",
        message="Emergency units have been alerted. Police control room is tracking your location.",
        dispatch_id=dispatch_id
    )


@router.get("/services", response_model=List[WelfareService])
async def get_welfare_services(category: Optional[str] = None):
    """
    Get list of available welfare services.
    Optional filter by category (e.g., 'emergency', 'legal').
    """
    if category:
        return [s for s in WELFARE_SERVICES if s.category == category]
    return WELFARE_SERVICES
