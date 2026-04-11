1. **Optimize array filtering and stats calculations in multiple Judge Persona components**
   - Several components inside `src/personas/judge/pages/` perform array filtering (`MOCK_CASES.filter`, etc.) directly in the component body. This causes unnecessary recalculation on every render.
   - For string searches, `toLowerCase()` is being called inside the filter loop, adding an $O(N)$ overhead per render.
   - I have already added `React.useMemo` to `CaseQueuePage`, `EvidenceVault`, `OrdersHistory`, `SmartBailPage`, `LegalKnowledgeBank`, and `BenchMemoTemplates` to wrap these calculations.
   - I have hoisted `search.toLowerCase()` outside the `.filter` callbacks so it is computed once per render rather than once per array item.
   - I moved `stats` calculation in `OrdersHistory` into `useMemo` as well to prevent recalculation.

2. **Run lint and build checks**
   - Execute `pnpm lint` (or `npm run lint`) to ensure no issues were introduced.
   - Execute `npm run build` or TS checks to verify build is safe.

3. **Complete pre-commit steps to ensure proper testing, verification, review, and reflection are done.**
   - Run the pre commit instructions and follow them carefully.
   - Ensure the performance gains are clearly documented in the PR description as required by Bolt's persona.

4. **Submit PR**
   - Submit the PR with the required Bolt format.
