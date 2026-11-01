## 2024-11-01 - Initializing Journal
**Learning:** Establishing the journal for tracking critical insights.
**Action:** Use this file to log significant performance findings specific to the codebase.

## 2024-11-01 - React.memo Gotcha in CaseIntakeTriage
**Learning:** When using React.memo on a list item like `CaseCard` that expects an `onSelect` callback, make sure the callback passed from the parent isn't recreated on every render (e.g. `onSelect={() => handleCaseSelect(caseData)}`). This completely defeats the memoization.
**Action:** Extract the callback to `useCallback` in the parent, and pass down the item ID (or the item itself) to the child so that the child can call it without needing inline arrow functions in the render loop.
