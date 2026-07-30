## 2024-07-30 - [Performance] Refactoring useState/useEffect for derived state
**Learning:** Found a common pattern where `useState` and `useEffect` are used together to compute derived state (like `filteredCases`), which causes double re-renders (one for the state dependency changing, another when the derived state is set).
**Action:** Always refactor derived state computation into `useMemo` when possible to prevent double re-renders, improve performance, and make the code simpler.
