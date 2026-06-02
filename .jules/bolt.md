## 2024-06-02 - [Missing Memoization Pattern]
**Learning:** [Frontend components such as CaseQueuePage, EvidenceVault, SmartBailPage, JudgeDashboard, and CitizenTimeline often recalculate derived arrays like filteredCases on every render. This missing memoization is a prime opportunity for React performance optimization.]
**Action:** [I will wrap these array derivations in useMemo to prevent unnecessary recalculations.]
