## 2024-05-24 - Avoid useState/useEffect for Derived Data Filtering
**Learning:** Using a combination of `useState` and `useEffect` to manage filtered arrays (like `filteredCases` based on `allCases` and filter options) is a performance anti-pattern. It triggers an unnecessary double re-render when dependencies change.
**Action:** Use `useMemo` to directly compute derived arrays instead, saving a render cycle.
