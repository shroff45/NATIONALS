## 2024-05-24 - React useMemo Optimization
**Learning:** Found an anti-pattern in `CaseIntakeTriage.tsx` where a `useState` and `useEffect` combination is used to manage the `filteredCases` array derived from `allCases`. This causes unnecessary double re-renders when state dependencies change.
**Action:** Replace the `useState`/`useEffect` pattern with a `useMemo` hook to directly derive `filteredCases`, improving React performance and code cleanliness.
