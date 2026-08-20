## 2024-08-20 - Derived State Anti-Pattern
**Learning:** The codebase contains a recurring React performance anti-pattern where derived arrays are managed using a useState and useEffect combination.
**Action:** Use the useMemo hook to directly derive the array during render, eliminating the extra render cycle.
