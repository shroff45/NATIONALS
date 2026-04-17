## 2026-04-17 - Optimization: Missing useMemo on React filtering
**Learning:** The codebase consistently lacks `useMemo` wrapping around array filtering and mapping operations inside React components (e.g., `filteredCases`, `filteredOrders`). This causes \(O(N)\) filtering logic to re-run on every render, which becomes a bottleneck.
**Action:** Wrap list filtering logic in `useMemo` with proper dependency arrays to prevent unnecessary re-computations and optimize performance.
