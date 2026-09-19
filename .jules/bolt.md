## 2024-01-20 - React Array Filter Memoization
**Learning:** Found multiple instances where array `.filter()` was being called directly inside component render functions (e.g., in `SmartBailPage`, `EvidenceVault`, `CaseQueuePage`). This creates a new array reference on every render, which can cause child components to unnecessarily re-render and degrade performance, especially with large lists.
**Action:** Always wrap expensive list filtering and transformations in `useMemo` with appropriate dependency arrays.
