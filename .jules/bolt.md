## 2024-05-28 - Lazy Evaluation of NetworkX Path Generators
**Learning:** Fully materializing `networkx` path generators (like `nx.all_simple_paths`) using `list()` can result in exponential memory allocation and $O(M)$ performance regressions for large or dense graphs.
**Action:** Always use lazy evaluation mechanisms such as `itertools.islice()` when limiting the output of deep graph traversal paths. Similarly, cache expensive recomputations like `nx.simple_cycles()` when they are needed across multiple iterations.
