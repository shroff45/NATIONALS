with open("backend/test_auth.py", "r") as f:
    content = f.read()

content = content.replace("            if test_protected_route(token):", "            if verify_protected_route(token):")

with open("backend/test_auth.py", "w") as f:
    f.write(content)
