## 2024-05-24 - React Derived State Anti-Pattern
**Learning:** Found a codebase-specific pattern where derived data (e.g., filtered arrays) is managed via `useState` and `useEffect`. This triggers an initial render followed by an immediate second render when the effect updates the state.
**Action:** Always prefer `useMemo` for derived data arrays based on existing state/props to compute the value during the render phase and eliminate the extra render cycle.
