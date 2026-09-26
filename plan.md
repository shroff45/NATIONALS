1. **Analyze Frontend Bottlenecks**:
The `CaseTriage.tsx` component is rendering a list of cases using `cases.map`. Within this map, there is an inline function being created for each item: `onClick={() => { setSelectedCase(c); onSelectCase(c); setPrediction(null); }}`. This causes every single item in the list to re-render whenever the parent component re-renders (e.g. when `selectedCase`, `loading`, or `prediction` state changes) because the inline function is a new reference every time.

2. **Implement Optimization**:
To resolve this, we can extract the list item into its own component `CaseItem` and wrap it in `React.memo`. We can also utilize `useCallback` for the click handler. This will significantly improve performance by avoiding unnecessary re-renders of the list items when the parent component's state changes.

   - File to edit: `nyayasahayak-main-main/src/modules/judge/features/CaseTriage.tsx`
   - Actions:
     - Import `memo` and `useCallback` from 'react'.
     - Extract the case card rendering logic into a new component named `CaseItem` wrapped in `React.memo`.
     - Define a `handleCaseClick` function using `useCallback` in the parent component.
     - Replace the `cases.map(...)` body with the `CaseItem` component.

3. **Verify the change**:
   - Run type checking using `cd nyayasahayak-main-main && npx typescript/tsc --noEmit`.

4. **Complete pre-commit steps to ensure proper testing, verification, review, and reflection are done.**

5. **Submit the Pull Request**:
   - Create a branch and commit the changes with the required Bolt PR format:
     - Title: "⚡ Bolt: [performance improvement]"
     - Description: Include What, Why, Impact, and Measurement details.
