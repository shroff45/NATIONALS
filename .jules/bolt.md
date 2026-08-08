## 2024-05-15 - CaseIntakeTriage Derived State Optimization
**Learning:** Found a classic React anti-pattern in `CaseIntakeTriage.tsx`: managing derived state (`filteredCases`) using a combination of `useState` and `useEffect`. When filter dependencies change, React renders twice: once for the dependency change, and again when the effect calls `setFilteredCases`.
**Action:** Replace `useState` + `useEffect` with a single `useMemo` hook that directly returns the derived array, eliminating the unnecessary double re-render.
