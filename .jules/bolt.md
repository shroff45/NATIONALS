## 2024-05-24 - Init\n**Learning:** Started looking for performance bottlenecks.\n**Action:** Will look for unoptimized React components.
## 2024-05-24 - React anti-pattern: useEffect for derived state
**Learning:** Found a common anti-pattern where a `useState` and `useEffect` combination is used to manage derived arrays (like `filteredCases`) instead of using `useMemo`. This causes unnecessary double re-renders whenever the filter dependencies change.
**Action:** Will refactor this pattern by directly yielding the derived array using a `useMemo` hook instead to optimize React performance and prevent unnecessary re-renders.
