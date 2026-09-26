## 2024-09-26 - Initial Setup
**Learning:** Initializing journal to track codebase-specific performance patterns.
**Action:** Use this file to log critical architectural performance insights.
## 2024-09-26 - Prevent Re-renders in CaseTriage List
**Learning:** Found an inline arrow function in a large case mapping list which causes O(N) components to re-render whenever the parent component state (e.g. selected case) changes.
**Action:** Always extract list items into a component wrapped in `React.memo` and pass callbacks wrapped in `useCallback` when lists can be long or components complex.
