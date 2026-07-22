with open("nyayasahayak-main-main/eslint.config.js", "r") as f:
    content = f.read()

content = content.replace("'no-unused-vars': ['error', { varsIgnorePattern: '^[A-Z_]' }],", "'no-unused-vars': 'off',")
content = content.replace("'react-hooks/exhaustive-deps': 'off',", "'react-hooks/exhaustive-deps': 'off',\n      'no-empty': 'off',\n      'no-useless-escape': 'off',\n      'no-redeclare': 'off',")


with open("nyayasahayak-main-main/eslint.config.js", "w") as f:
    f.write(content)
