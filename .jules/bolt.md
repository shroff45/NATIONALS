## 2024-05-18 - Avoid nx.simple_cycles inside loops for FinancialAnalyzer
**Learning:** Calling `nx.simple_cycles(self.graph)` inside a node iteration loop scales horrendously on large graphs (O(N * (V+E)*C)). The `FinancialAnalyzer._detect_shell_companies` was doing exactly this.
**Action:** Replace `nx.simple_cycles` inside loops with a one-time calculation of `nx.strongly_connected_components(self.graph)` outside the loop, storing nodes that belong to a component of size > 1 (or have self-loops) into a set for fast O(1) membership checking.
