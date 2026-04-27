## 2025-05-15 - React Performance OrdersHistory
**Learning:** Consolidating three O(N) array `.filter` iterations into a single `.reduce` pass significantly reduces time complexity and CPU cycle usage during re-renders.
**Action:** Always identify repeated iterations over static or large arrays within render loops and memoize their aggregated results.
