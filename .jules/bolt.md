## 2025-01-20 - Memoizing list filter in CaseQueuePage
**Learning:** In `CaseQueuePage.tsx`, the `filteredCases` array is recalculated on every render, even when `search` or `filter` states haven't changed (e.g. when `selectedCase` changes). This causes unnecessary re-renders of the list.
**Action:** Wrap `filteredCases` in `useMemo` and hoist the `search.toLowerCase()` operation out of the filter loop.
