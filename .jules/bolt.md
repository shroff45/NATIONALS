## 2026-04-18 - ESLint Flat Config Export Error
**Learning:** In ESLint 8.57.1, importing `defineConfig` from `'eslint/config'` causes an `[ERR_PACKAGE_PATH_NOT_EXPORTED]` error because the `./config` subpath is missing.
**Action:** When configuring ESLint Flat Config in this repository, export the config array directly (e.g., `export default [ ... ]`) instead of using `defineConfig`.

## 2026-04-18 - Pytest Exit Code 5 in CI
**Learning:** Pytest returns exit code 5 when no tests are collected. If a CI pipeline runs pytest against a directory (e.g., `app/`) that might legitimately have zero tests, this exit code will cause the CI to fail incorrectly.
**Action:** Append `|| [ 0 -eq 5 ]` to the pytest bash command in the CI workflow to explicitly permit the 'No tests collected' exit code without masking genuine test failures (exit code 1).
