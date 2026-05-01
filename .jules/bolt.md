## 2026-05-01 - [NetworkX Path and Cycle Materialization Pitfalls]
**Learning:** Fully materializing `nx.all_simple_paths` with `list()` before slicing causes exponential time/memory blowups in dense graphs. Similarly, calling `nx.simple_cycles` inside a loop recalculates the entire cycle set O(N) times.
**Action:** Always use `itertools.islice` to lazily evaluate graph paths when only a subset is needed. Cache expensive whole-graph operations like cycle detection outside of node iteration loops.
