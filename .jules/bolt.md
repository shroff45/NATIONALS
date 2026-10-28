
## $(date +%Y-%m-%d) - Prevent unnecessary list re-renders
**Learning:** Extracting inline arrow functions and React elements from list `map` iterations into `React.memo` components with `useCallback` effectively minimizes wasteful re-renders. This is particularly critical in complex layouts like JudgeDashboard where parent component state updates frequently (e.g. activeTab, selectedCase, loading state).
**Action:** Always identify lists with inline elements/functions in `.tsx` files and refactor them by lifting the element to a typed `React.memo` component and passing memoized handlers. Ensure to define strict prop interfaces before the component definition.
