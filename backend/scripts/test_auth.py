import requests

BASE_URL = "http://localhost:8000/api/v1"

def test_auth_endpoints():
    print("Testing Auth Endpoints...")

    # Register Citizen
    response = requests.post(f"{BASE_URL}/auth/register", json={
        "email": "citizen@test.com",
        "password": "password123",
        "role": "CITIZEN",
        "full_name": "Test Citizen"
    })
    print(f"Register Citizen: {response.status_code}")

    # Login Citizen
    response = requests.post(f"{BASE_URL}/auth/login", data={
        "username": "citizen@test.com",
        "password": "password123"
    })
    print(f"Login Citizen: {response.status_code}")

    if response.status_code == 200:
        token = response.json().get("access_token")

        # Test Me endpoint
        headers = {"Authorization": f"Bearer {token}"}
        me_response = requests.get(f"{BASE_URL}/auth/me", headers=headers)
        print(f"Get Profile: {me_response.status_code}")

if __name__ == '__main__':
    test_auth_endpoints()
