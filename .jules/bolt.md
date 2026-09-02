## 2026-09-02 - Array Filtering in React Renders
**Learning:** In a codebase heavily relying on mock data filtering directly in the render function (like CaseQueuePage), leaving these unfiltered creates an O(N) recalculation on every re-render. Since `MOCK_QUEUE` is hardcoded but filtering logic involves string searches and type matches, this gets increasingly expensive.
**Action:** Always wrap array filter/map operations in React components with `useMemo` when they depend on state variables like `search` and `filter` to prevent unnecessary main thread blocking on large datasets.
