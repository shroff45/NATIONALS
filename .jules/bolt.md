## 2025-05-17 - Optimize NetworkX Graph Analysis
**Learning:** Fully materializing `networkx` generators like `nx.all_simple_paths` (e.g., using `list()`) and unnecessarily recomputing algorithms like `nx.simple_cycles` inside loops can lead to exponential time $O(V+C)$ and memory $O(2^V)$ consumption on dense graphs.
**Action:** Use `itertools.islice()` to lazily evaluate generators and limit paths, and proactively cache expensive graph computations (like finding simple cycles) outside of iterative node or edge processing logic.
