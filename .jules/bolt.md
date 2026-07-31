## 2026-07-31 - Refactored double-render anti-pattern in CaseIntakeTriage
**Learning:** This codebase contains a common React performance anti-pattern where a `useState` + `useEffect` combination is used to manage derived arrays like `filteredCases`. This causes unnecessary double re-renders when state dependencies change.
**Action:** Use `useMemo` to directly yield derived arrays instead of managing them via a separate state variable updated inside an effect.
