## 2024-05-26 - Lazy Evaluation of NetworkX Generators
**Learning:** Found that fully materializing graph generators like `nx.all_simple_paths` and `nx.simple_cycles` inside loops was causing potential $O(2^V)$ or $O(V+E)$ regressions in backend analytical services (`financial_service.py`) during dense graph operations.
**Action:** Always wrap limited-output path queries in `itertools.islice` instead of `list(generator)[:N]`, and cache expensive full-graph evaluations (like cycle detection) outside of node iterations when their output can be reused.
## 2024-05-26 - Pytest Collection and ESLint Flat Config Issues
**Learning:** Found that `pytest` fails test collection with `SystemExit: 1` if a helper function is named with a `test_` prefix (like `test_endpoint`) and runs top-level execution code directly. Also found that ESLint v9+ flat configs (`eslint.config.js`) will fail fatally if run using the deprecated `--ext ts,tsx` CLI flag.
**Action:** Rename pytest helper functions to `verify_` (e.g., `verify_endpoint`), wrap script execution logic in `if __name__ == '__main__':`, and remove `--ext` flags from `package.json` lint scripts when migrating to flat configs.
