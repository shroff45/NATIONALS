## 2024-03-24 - React List Rendering Bottleneck
**Learning:** Using inline arrow functions in event handlers (e.g., `onClick={() => setCase(c)}`) within mapping or rendering large lists causes the child components to re-render constantly because the function reference changes on every parent render.
**Action:** Extract list items into their own memoized components (`React.memo`) or use `useCallback` effectively, ensuring no new function references are passed down as props during renders.
