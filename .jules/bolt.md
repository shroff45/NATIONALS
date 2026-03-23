## 2026-03-23 - Graph algorithm optimization in Financial Analyzer
**Learning:** Running expensive pathfinding algorithms like `nx.simple_cycles` inside node iteration loops causes severe O(N * (V+E)*C) performance degradation for graph-based anomaly detection.
**Action:** Compute global metrics like `nx.strongly_connected_components` once (O(V+E)) rather than executing pathfinding within node loops.
