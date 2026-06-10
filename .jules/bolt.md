## 2024-06-10 - Initial Setup
**Learning:** Initializing journal for performance learnings.
**Action:** Keep track of performance optimization lessons here.
## 2024-06-10 - Unnecessary Re-renders in Case Queue Page
**Learning:** Found several pages (e.g., CaseQueuePage.tsx, EvidenceVault.tsx, SmartBailPage.tsx, CitizenTimeline.tsx) filtering mock arrays directly in the render function. This causes the array to be re-created on every render, even when the search query or filter hasn't changed.
**Action:** Always wrap derived lists in `useMemo` and hoist repetitive string operations like `.toLowerCase()` out of the loop.
