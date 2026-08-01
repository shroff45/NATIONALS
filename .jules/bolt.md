## 2024-05-30 - Anti-pattern: Derived state via useEffect
**Learning:** In CaseIntakeTriage (and similar components), filtering a list in a useEffect and storing the result in a local state variable causes double re-renders (one for the dependency change, one for the state update).
**Action:** Use useMemo to compute derived arrays directly during render to save unnecessary re-renders.
