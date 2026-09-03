## 2024-05-13 - [Init]
**Learning:** Initializing journal.
**Action:** Use journal to record learnings.
## 2024-05-13 - [React Performance Optimization]
**Learning:** Found multiple un-memoized callback functions in MainApp.tsx being passed down to large, potentially complex React components (like Nyayabot, CaseIntakeTriage, DocumentAnalysis), causing unnecessary child re-renders on state changes (e.g. activeTab, chatHistory).
**Action:** Used useCallback on functions like `logActivity`, `handleSignIn`, `handleSignOut`, `clearActivityHistory`, and `handleSetChatHistory` to ensure referential stability and prevent unnecessary deep re-renders, while maintaining empty dependency arrays where appropriate by utilizing state updater functions (`setActivityHistory(prev => ...)`).
