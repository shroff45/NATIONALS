## 2026-03-31 - Graph algorithm optimization in node iterations
**Learning:** Found an O(N * (V+E) * C) performance bottleneck where nx.simple_cycles was calculated inside a node loop in FinancialAnalyzer.
**Action:** Use lazy evaluation outside the loop to compute cycles only once, converting the result to an O(1) lookup set (nodes_in_cycles_set), reducing complexity to O((V+E) * C + N).
