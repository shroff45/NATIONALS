## 2024-05-24 - Initialization
**Learning:** Initialized Bolt journal.
**Action:** Proceed with performance optimization.
## 2024-05-24 - CaseIntakeTriage optimization
**Learning:** Derived arrays created with `filter` inside `useEffect` with a `useState` backing store is a common anti-pattern that leads to unnecessary double re-renders in React when dependencies change.
**Action:** Replaced with a single `useMemo` computation which computes the `filteredCases` array locally directly when dependencies change.
