## 2025-02-19 - Removed unnecessary effect for derived state
**Learning:** Found a common performance anti-pattern in `CaseIntakeTriage.tsx` where derived data (`filteredCases`) is maintained via a combination of `useState` and `useEffect`. This pattern causes unnecessary double re-renders (one for the dependency state, another for the effect updating the filtered list).
**Action:** Always prefer `useMemo` for derived arrays instead of `useEffect` to avoid extra renders and improve responsiveness on filter changes.
