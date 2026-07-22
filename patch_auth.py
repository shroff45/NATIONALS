with open("backend/test_auth.py", "r") as f:
    content = f.read()

content = content.replace("def test_protected_route(token):", "def verify_protected_route(token):")
content = content.replace("    test_protected_route(token)", "    verify_protected_route(token)")

with open("backend/test_auth.py", "w") as f:
    f.write(content)
