## 2024-05-24 - Avoid Graph Algorithms in Node Loops
**Learning:** In `FinancialAnalyzer` within `backend/app/services/financial_service.py`, invoking complex algorithms like `nx.simple_cycles` inside per-node iterations causes severe $O(V \times (V+E) \times C)$ performance degradation.
**Action:** Instead, calculate global metrics like `nx.strongly_connected_components` once ($O(V+E)$) globally outside the loop and reuse the findings.
