## 2024-05-24 - React useEffect Anti-pattern for Derived State
**Learning:** Using useState and useEffect to manage derived state (like filtered lists) causes unnecessary double re-renders. Additionally, expensive string operations like `.toLowerCase()` inside filter loops can degrade performance.
**Action:** Always use useMemo for deriving state based on props or other state variables. Hoist expensive operations like string conversions outside of iteration loops to avoid redundant processing.
