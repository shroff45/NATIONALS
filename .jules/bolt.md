## 2024-07-05 - Missing useMemo in React components
**Learning:** The frontend React components like CaseIntakeTriage manage derived array state using `useEffect` and `useState` (e.g. filteredCases). This leads to unnecessary state updates and re-renders when dependencies change.
**Action:** Use `useMemo` for derived states to prevent unnecessary updates and improve performance, which is a common optimization for list components.
