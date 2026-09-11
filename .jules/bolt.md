## 2024-12-05 - Missing Memoization on Filtered Lists
**Learning:** Found multiple instances where large lists or arrays are filtered directly in the component body during render, causing unnecessary re-calculations on every render cycle. `MOCK_ORDERS.filter` in `OrdersHistory.tsx` is one example.
**Action:** When filtering or sorting data derived from state or props, always wrap the operation in a `useMemo` hook to ensure the calculation only runs when dependencies change, avoiding unnecessary overhead during re-renders.
