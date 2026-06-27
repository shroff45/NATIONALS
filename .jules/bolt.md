## 2024-06-27 - Hoist toLowerCase() calls outside of array iteration
**Learning:** Found multiple instances where `toLowerCase()` is called repeatedly on search queries inside `filter` or `map` loops (e.g. `CaseIntakeTriage.tsx`, `JudgeDashboard.tsx`), which is an O(N) redundant operation. This impacts rendering performance, especially for large lists of data.
**Action:** Always hoist `.toLowerCase()` or other invariant transformations outside of loops to prevent unnecessary recalcuations on every iteration. Use `useMemo` and extract derivations.
