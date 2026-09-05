## 2024-03-01 - Bolt Initialized
**Learning:** Initialized Bolt performance journal.
**Action:** Ready to track critical performance learnings.
## 2024-03-01 - Missing React.memo on complex view components
**Learning:** High-impact view components like History and CaseRelationshipMapper in this architecture are frequently missing memoization, leading to unnecessary re-renders of lists and SVG layers on parent state changes.
**Action:** Always verify if export components processing arrays or complex DOM elements are wrapped in React.memo().
