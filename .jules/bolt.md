
## 2026-10-28 - Prevent unnecessary list re-renders
**Learning:** Extracting inline arrow functions and React elements from list `map` iterations into `React.memo` components with `useCallback` effectively minimizes wasteful re-renders. This is particularly critical in complex layouts like JudgeDashboard where parent component state updates frequently (e.g. activeTab, selectedCase, loading state).
**Action:** Always identify lists with inline elements/functions in `.tsx` files and refactor them by lifting the element to a typed `React.memo` component and passing memoized handlers. Ensure to define strict prop interfaces before the component definition.

## 2026-10-28 - Prevent Pytest Collection Errors in Integration Scripts
**Learning:** Pytest aggressively collects any file matching `test_*.py` and any function matching `test_*()` within those files. If you have manual integration scripts (like `backend/test_endpoints.py` or `backend/test_auth_comprehensive.py`) that make real HTTP requests or lack actual pytest fixtures, pytest will crash when trying to collect or execute them during the CI build process.
**Action:** Always name helper/integration script functions with a prefix like `verify_*` instead of `test_*` to avoid accidental collection by pytest. Ensure that all top-level script execution logic (e.g. `success = True; verify_endpoint(...)`) is properly guarded within an `if __name__ == "__main__":` block to prevent execution on module import.
