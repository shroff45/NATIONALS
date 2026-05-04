## 2025-02-23 - Lazy Evaluation of NetworkX Generators
**Learning:** Fully materializing `networkx` generators like `nx.all_simple_paths` or computing expensive operations like `nx.simple_cycles` multiple times inside loops can cause exponential time/memory regressions on dense graphs.
**Action:** Always use `itertools.islice()` to lazily evaluate paths when only a limited number are needed, and cache expensive computations like `simple_cycles` using a lazy initialization pattern (`if cycles is None:`) before loops or inside loops only when thresholds are met.
