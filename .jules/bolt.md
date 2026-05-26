## 2024-05-26 - Lazy Evaluation of NetworkX Generators
**Learning:** Found that fully materializing graph generators like `nx.all_simple_paths` and `nx.simple_cycles` inside loops was causing potential $O(2^V)$ or $O(V+E)$ regressions in backend analytical services (`financial_service.py`) during dense graph operations.
**Action:** Always wrap limited-output path queries in `itertools.islice` instead of `list(generator)[:N]`, and cache expensive full-graph evaluations (like cycle detection) outside of node iterations when their output can be reused.
## 2024-05-26 - Pytest Collection and ESLint Flat Config Issues
**Learning:** Found that `pytest` fails test collection with `SystemExit: 1` if a helper function is named with a `test_` prefix (like `test_endpoint`) and runs top-level execution code directly. Also found that ESLint v9+ flat configs (`eslint.config.js`) will fail fatally if run using the deprecated `--ext ts,tsx` CLI flag.
**Action:** Rename pytest helper functions to `verify_` (e.g., `verify_endpoint`), wrap script execution logic in `if __name__ == '__main__':`, and remove `--ext` flags from `package.json` lint scripts when migrating to flat configs.

## 2024-05-26 - ESLint Flat Config Plugin Compatibility
**Learning:** Older ESLint plugins (like `eslint-plugin-react-hooks@4.6.2`) do not expose a `.configs.flat` property. Attempting to use them directly in a flat config array (e.g. `reactHooks.configs.flat.recommended`) causes a fatal `TypeError` during linting.
**Action:** When migrating older plugins to ESLint Flat Config, manually configure them by mapping the imported plugin object inside the `plugins` key (e.g. `plugins: { 'react-hooks': reactHooks }`) and manually spreading their rule definitions in the `rules` object.
