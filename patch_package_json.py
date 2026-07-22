import json

with open("nyayasahayak-main-main/package.json", "r") as f:
    data = json.load(f)

data["scripts"]["lint"] = "eslint . --report-unused-disable-directives --max-warnings 0"

with open("nyayasahayak-main-main/package.json", "w") as f:
    json.dump(data, f, indent=4)
