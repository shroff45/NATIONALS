with open("backend/scripts/test_api_endpoints.py", "r") as f:
    content = f.read()

content = content.replace("def test_", "def verify_")
content = content.replace("test_health()", "verify_health()")
content = content.replace("test_registry_scrutiny()", "verify_registry_scrutiny()")
content = content.replace("test_registry_fees()", "verify_registry_fees()")
content = content.replace("test_listing_pending()", "verify_listing_pending()")
content = content.replace("test_listing_optimize()", "verify_listing_optimize()")


with open("backend/scripts/test_api_endpoints.py", "w") as f:
    f.write(content)
