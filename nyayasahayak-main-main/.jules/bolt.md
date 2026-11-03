## 2024-11-03 - React.memo Optimization
**Learning:** In React, applying `React.memo` along with `useCallback` for prop functions is an effective way to optimize list rendering. However, when refactoring inline functions in components like `CaseIntakeTriage.tsx`, the child component must be extracted and correctly typed, and parent references must use `useCallback`.
**Action:** Always wrap list child components with `React.memo` when there are complex lists and avoid inline functions in the `render` path to reduce re-renders.
