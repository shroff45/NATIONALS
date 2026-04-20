## 2026-04-20 - [Bolt] OrdersHistory filtering reduction
**Learning:** The application previously performed multiple `array.filter(...).length` passes over static arrays inside JSX blocks on every render for statistics footers. Converting these to a single memoized `reduce` pass improves performance from O(K*N) to O(N).
**Action:** Always use `useMemo` and `reduce` to combine multiple filter conditions on the same array instead of repeating array traversals inside JSX rendering logic.
