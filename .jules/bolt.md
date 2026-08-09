## 2026-08-09 - [Replace useState/useEffect with useMemo for Derived Data]
**Learning:** In CaseIntakeTriage.tsx, `filteredCases` is derived state created via `useState` and updated via an effect dependent on `searchTerm`, `activeCaseType`, and `activePriority`. This anti-pattern causes an initial double render: 1 for search/filter changes, and 1 for the `setFilteredCases` update in the effect.
**Action:** Consistently use `useMemo` to derive list filters instead of syncing them to state via `useEffect`.
