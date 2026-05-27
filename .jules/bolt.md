## 2024-05-27 - Lazily evaluate NetworkX paths
**Learning:** In the backend `financial_service.py`, using `list(nx.all_simple_paths(...))` before slicing (e.g., `[:5]`) forces NetworkX to compute all possible simple paths. For dense graphs, this causes exponential $O(V!)$ time and memory consumption, leading to severe performance bottlenecks.
**Action:** Use `itertools.islice(nx.all_simple_paths(...), 5)` to lazily evaluate generators, stopping computation exactly when the required number of paths is found.
## 2024-05-27 - Fixing ESLint flat config CLI options
**Learning:** In ESLint v9 (and when using flat config `eslint.config.js` in v8), the CLI flag `--ext` is completely unsupported and will cause lint scripts to fail with an `Invalid option '--ext'` error, breaking the CI pipeline.
**Action:** Remove `--ext ts,tsx` from the `npm run lint` script and explicitly define the allowed file extensions inside the `files` array of the exported configuration objects in `eslint.config.js`.

## 2024-05-27 - Fixing Pytest collection errors on integration test scripts
**Learning:** Top-level execution logic (like `sys.exit(1)`) in standalone integration testing scripts (e.g., `test_endpoints.py`) will trigger and prematurely abort the `pytest` collection process, causing the CI suite to fail completely. Furthermore, helper methods like `test_endpoint(name, url)` will be mistakenly collected as tests requiring fixtures.
**Action:** Always protect top-level script execution with `if __name__ == '__main__':`, and rename helper methods from `test_` to `verify_` (e.g., `verify_endpoint`) to avoid accidental test collection.
