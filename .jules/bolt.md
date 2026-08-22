## 2024-05-20 - [React Performance: Derived State Anti-Pattern]
**Learning:** The codebase used a useState+useEffect combination to manage `filteredCases` which causes unnecessary double re-renders whenever a dependency changes. This pattern was found in `CaseIntakeTriage`.
**Action:** Used `useMemo` to compute derived state directly during render to avoid the extra render cycle and improve performance.
