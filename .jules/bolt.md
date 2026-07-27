## 2026-07-27 - [React Optimization: useState/useEffect to useMemo]
**Learning:** Refactoring useState/useEffect used for derived arrays (like filteredCases) into a useMemo hook prevents double re-renders when state dependencies change.
**Action:** Always prefer useMemo over useState/useEffect for computing derived lists based on state/props.
