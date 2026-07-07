## 2025-02-23 - Missing Memoization in Derived Arrays
**Learning:** Found that `CaseQueuePage.tsx` recomputes `filteredCases` on every render, even when irrelevant state like `selectedCase` changes. The list involves string methods like `.toLowerCase()` which are slow when mapping over arrays.
**Action:** Always wrap derived filtering logic with `useMemo` and hoist repetitive string normalizations out of the loop, specifically in this codebase where `MOCK_QUEUE` data arrays are present.
