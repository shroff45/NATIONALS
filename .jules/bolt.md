## 2025-02-12 - Prevented full list re-renders on selection
**Learning:** In complex mapping logic where a selected state dictates styling of list items, directly using inline arrow handlers in `.map` (e.g. `onClick={() => setSelection(item)}`) breaks reference equality. Extracting the list item into a `React.memo` component and passing a `useCallback` handler is necessary.
**Action:** Always extract list items into `React.memo` components and use `useCallback` for selection handlers when rendering long lists.
