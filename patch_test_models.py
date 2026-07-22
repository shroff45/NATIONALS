import re

with open("nyayasahayak-main-main/test-models.ts", "r") as f:
    content = f.read()

content = content.replace("const models toTry = ['gemini-1.5-flash'", "const models = ['gemini-1.5-flash'")

with open("nyayasahayak-main-main/test-models.ts", "w") as f:
    f.write(content)
