## 2025-02-28 - Unmemoized Array Filtering
**Learning:** Found a common pattern in the frontend where arrays (like `filteredCases`) are derived directly in the render body using `.filter()`. Without memoization, this causes O(N) recalculations on every single render, which can scale poorly when mock lists are replaced with real API data.
**Action:** Always wrap array filtering/derivations in `useMemo` with appropriate dependency arrays when building or optimizing React components that render lists.
