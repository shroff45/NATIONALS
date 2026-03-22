
## 2025-03-09 - Avoid Graph Cycle Detection Inside Node Iterations
**Learning:** Calling `networkx.simple_cycles` inside a `graph.nodes()` iteration loops causes severe O(N * (V+E)*C) performance degradation for graph algorithms like shell company detection in `FinancialAnalyzer`, especially since `simple_cycles` can grow exponentially for dense graphs.
**Action:** Extract cycle/connected component detection out of loops. Cache structural properties globally (like using lazy-evaluation of `nx.strongly_connected_components` mapping to a lookup set of valid cyclic nodes which scales linearly O(V+E)) before running node-level iterations.
