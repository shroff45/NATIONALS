## 2025-05-18 - Single Loop Optimization in React
**Learning:** Found multiple separate `Array.filter().length` calls inside a React functional component's render body that recalculate on every re-render (e.g., when typing in a search bar).
**Action:** Combine multiple `O(n)` array traversals into a single `O(n)` loop inside a `useMemo` block, especially when calculating derived static data, reducing redundant computations on state updates.
