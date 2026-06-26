## 2024-05-15 - Missing Memoization in Frontend Lists
**Learning:** React list components (like `CaseQueuePage.tsx`, `EvidenceVault.tsx`, etc.) are filtering arrays directly in the render cycle without `useMemo`, which causes unnecessary recalculations on every render.
**Action:** Wrap derived arrays (like `filteredCases`) in `useMemo` with explicit dependencies to optimize React performance and prevent unnecessary re-renders when unrelated state changes.
