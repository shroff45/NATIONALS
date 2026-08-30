## 2023-10-27 - Memoize Case Filters in Queue Views
**Learning:** Found that `CaseQueuePage.tsx` re-calculated filtered lists on every render, such as when selecting a case, which causes redundant computations over static mock data.
**Action:** Used `useMemo` for filtering operations that depend on search and filter states to prevent unnecessary re-computations when selecting items.
