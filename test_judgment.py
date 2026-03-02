import requests
import json

response = requests.post('http://localhost:8000/api/v1/judge/judgment/test-validate')
print("Status Code:", response.status_code)
print("Response JSON:")
print(json.dumps(response.json(), indent=2))
