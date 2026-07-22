with open("backend/test_endpoints.py", "r") as f:
    content = f.read()

content = content.replace("        print(\"--- STARTING BACKEND INTEGRATION TESTS ---\\n\")",
    "    print(\"--- STARTING BACKEND INTEGRATION TESTS ---\\n\")")

with open("backend/test_endpoints.py", "w") as f:
    f.write(content)
