## 2025-02-12 - Prevent Double Re-renders in React
**Learning:** Derived state managed with `useState` and `useEffect` causes an initial render followed by an immediate re-render when the effect runs, negatively impacting performance.
**Action:** Always use `useMemo` to directly compute derived arrays from state variables during render instead of syncing them via `useEffect`.
