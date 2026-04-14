## 2026-04-14 - Prevent dependency additions for CI fixes
**Learning:** The prompt strictly forbids modifying package.json/tsconfig.json without explicit instruction, even if attempting to fix broken baseline CI tools (like eslint dependencies). Adding dependencies causes lockfile churn that pollutes the PR.
**Action:** Never try to "fix" broken linters or tests in a restricted baseline repository by modifying package.json unless explicitly told to do so.
