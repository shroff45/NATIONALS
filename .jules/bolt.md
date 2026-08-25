## 2024-05-18 - Refactoring useState/useEffect for derived state
**Learning:** Found a common React anti-pattern in the codebase: using `useState` combined with `useEffect` to manage a derived array (`filteredCases`). This causes an unnecessary double re-render whenever the search query or filters change: first when the state updates, and again when the effect runs and sets the filtered cases state.
**Action:** Always refactor derived state into a `useMemo` hook to compute the derived values dynamically instead of tracking them in separate state fields, thereby avoiding extra renders.
