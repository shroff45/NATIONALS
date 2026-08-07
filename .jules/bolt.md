## 2024-08-07 - React Performance Pattern
**Learning:** Found a common anti-pattern in the codebase: using `useState` and `useEffect` to manage derived arrays like `filteredCases` instead of `useMemo`. This causes double re-renders.
**Action:** Replace `useState`/`useEffect` combos for derived data with `useMemo` hooks.
