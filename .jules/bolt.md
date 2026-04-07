## 2024-05-15 - [Graph Cycle Detection Bottleneck]
**Learning:** Calling O((V+E)*C) pathfinding algorithms like `nx.simple_cycles` inside node iteration loops causes severe performance degradation O(N*(V+E)*C) in graph-based anomaly detection like the shell company pattern.
**Action:** Use global graph metrics like `nx.strongly_connected_components` (which is O(V+E)) computed once using lazy evaluation outside or at the top of loops to determine cycle membership. Include self-loops using `nx.selfloop_edges` for completeness.
