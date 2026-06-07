## 2025-02-12 - CaseQueuePage List Derivation
**Learning:** Frequent React unoptimized recalculations exist in list view components (e.g., CaseQueuePage). Filtering lists without `useMemo` triggers a full recount when unrelated state, such as `selectedCase`, changes, leading to unnecessary re-renders.
**Action:** When working on lists that support searching and filtering, always wrap the derivation array in `useMemo` with only the specific filter states as dependencies, and hoist repetitive operations like `toLowerCase` outside the loop.
