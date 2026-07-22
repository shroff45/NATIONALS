with open("backend/test_auth_comprehensive.py", "r") as f:
    content = f.read()

content = content.replace("def test(name, condition, details=\"\"):", "def verify(name, condition, details=\"\"):")
content = content.replace("    test(", "    verify(")
content = content.replace("test(", "verify(")
content = content.replace("def test_comprehensive_auth():", "if __name__ == '__main__':")

with open("backend/test_auth_comprehensive.py", "w") as f:
    f.write(content)
