## 2025-03-09 - [Optimize shell company cycle detection to O(V+E)]
**Learning:** Avoid calling expensive graph algorithms (like `networkx.simple_cycles`) inside node iterations. This leads to severe O(N * (V+E)*C) performance degradation.
**Action:** Precompute node memberships in cycles outside the loop using `nx.strongly_connected_components` (size > 1) and `nx.selfloop_edges`, which runs in O(V+E) time, and use O(1) set lookup inside the loop.
