## 2024-05-18 - Avoid useState/useEffect for Derived Arrays
**Learning:** Managing derived arrays with useState and useEffect causes unnecessary double re-renders.
**Action:** Use useMemo instead to compute and yield derived arrays directly.
