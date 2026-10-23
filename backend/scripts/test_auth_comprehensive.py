import requests

BASE_URL = "http://localhost:8000/api/v1"

def test_full_auth_flow():
    print("--- STARTING COMPREHENSIVE AUTH TEST ---")

    # 1. Test Unified Registration
    print("\n1. Testing Unified Registration (Citizen)")
    reg_data = {
        "email": "unified.citizen@test.com",
        "password": "securepassword123",
        "role": "CITIZEN",
        "full_name": "Unified Test Citizen",
        "phone_number": "+919876543210"
    }

    response = requests.post(f"{BASE_URL}/auth/register", json=reg_data)
    print(f"Status: {response.status_code}")
    if response.status_code not in [200, 400]: # 400 if already exists
        print(f"Error: {response.text}")

    # 2. Test Unified Login
    print("\n2. Testing Unified Login")
    login_data = {
        "username": "unified.citizen@test.com",
        "password": "securepassword123",
        "client_id": "CITIZEN" # Sending role as client_id for role verification
    }

    response = requests.post(f"{BASE_URL}/auth/login", data=login_data)
    print(f"Status: {response.status_code}")

    if response.status_code == 200:
        token_data = response.json()
        print("✅ Login successful. Received token.")

        # 3. Test Profile Fetch (Auth Context)
        print("\n3. Testing Profile Fetch (/me)")
        headers = {"Authorization": f"Bearer {token_data['access_token']}"}
        me_response = requests.get(f"{BASE_URL}/auth/me", headers=headers)

        print(f"Status: {me_response.status_code}")
        if me_response.status_code == 200:
            user_data = me_response.json()
            print(f"✅ Profile verified: {user_data.get('email')} ({user_data.get('role')})")
        else:
            print(f"❌ Profile fetch failed: {me_response.text}")
    else:
        print(f"❌ Login failed: {response.text}")

if __name__ == "__main__":
    test_full_auth_flow()
