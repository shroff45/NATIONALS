## 2024-05-20 - React useState/useEffect anti-pattern for derived state
**Learning:** Found a common codebase-specific performance anti-pattern where derived arrays (like filtered lists) are managed using a `useState` and `useEffect` combination. This causes unnecessary double re-renders whenever state dependencies change.
**Action:** Refactor this pattern by directly yielding the derived array using a `useMemo` hook instead. Ensure to import `useMemo` from 'react'.
