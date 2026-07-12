## 2024-05-19 - React Re-renders
**Learning:** Found multiple places in the frontend list components where `filter` operations are run synchronously in the component body instead of being memoized with `useMemo`. This leads to unnecessary computations on every re-render, especially since these components have other state changes (like `selectedCase`).
**Action:** When working on list views, always look out for derived state and memoize it. I'll optimize `CaseQueuePage.tsx` or `SmartBailPage.tsx` next.
