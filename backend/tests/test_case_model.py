from app.models.case import Case

def test_case_indexes():
    """
    Verify that critical columns in the Case model are indexed for performance.
    """
    # Check 'status' index
    status_col = Case.__table__.columns['status']
    assert status_col.index is True, "Status column should be indexed for faster filtering"

    # Check 'police_station_id' index
    police_station_col = Case.__table__.columns['police_station_id']
    assert police_station_col.index is True, "Police Station ID column should be indexed for faster filtering"
