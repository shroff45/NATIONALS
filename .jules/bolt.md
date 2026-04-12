## 2024-05-19 - [Optimize React Filtering]
**Learning:** Found repetitive O(N) array filtering in the render cycle, which can cause significant jank in React, especially in complex components like `VirtualMootCourt.tsx`.
**Action:** Always check array `.filter` and `.map` usage inside JSX, and memoize them using `useMemo` when they depend on state. Hoist string operations like `toLowerCase()` outside of loops.
