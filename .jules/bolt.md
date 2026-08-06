## 2025-08-06 - [React Performance Optimization]
**Learning:** Found multiple instances where array filtering is done directly inside the render cycle (e.g., in CaseQueuePage, EvidenceVault, CitizenTimeline) instead of using useMemo. This can cause unnecessary re-renders when state changes.
**Action:** Optimize one of these components by wrapping the filter logic in useMemo with explicit dependencies to prevent unnecessary recalculations on every render.
