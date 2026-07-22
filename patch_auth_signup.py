with open("backend/test_auth.py", "r") as f:
    content = f.read()

content = content.replace("def test_signup():", "def verify_signup():")
content = content.replace("    if test_signup():", "    if verify_signup():")
content = content.replace("def test_login():", "def verify_login():")
content = content.replace("        token = test_login()", "        token = verify_login()")

with open("backend/test_auth.py", "w") as f:
    f.write(content)
