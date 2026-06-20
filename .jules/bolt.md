## 2024-05-20 - Missing useMemo in List Components
**Learning:** Found that `filteredCases` in `CaseQueuePage` is calculated on every render.
**Action:** Use `useMemo` for derived arrays like `filteredCases` with explicit dependencies.
