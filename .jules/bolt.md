
## 2025-03-12 - [Optimizing NetworkX simple_cycles in loops]
**Learning:** Calling `nx.simple_cycles(graph)` inside an active node iteration in Python scales horribly ($O(N \times (V+E) \times C)$) because it calculates cycles across the entire graph repeatedly for every node evaluated. In `_detect_shell_companies` inside `financial_service.py`, this created a massive performance bottleneck on large graphs.
**Action:** When determining if nodes are part of a cyclic flow within a larger node-iteration block, compute the cyclic graph properties globally *outside the loop*. Use lazy evaluation and computationally cheaper alternative APIs, like `nx.strongly_connected_components`, which takes only $O(V+E)$ and completely eliminates the $O(N)$ multiplier and cyclic permutations calculations.
