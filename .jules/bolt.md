## 2024-05-25 - Prevent exponential memory/time consumption on dense graphs
**Learning:** Materializing generator paths using `list(nx.all_simple_paths(...))` inside a loop can be extremely costly on dense graphs with large number of permutations of pathing.
**Action:** Use `itertools.islice()` to lazily evaluate paths directly from the generator if you only need a subset (e.g. `islice(nx.all_simple_paths(...), 5)`). This prevents massive OOM and slow execution.

## 2024-05-25 - Prevent O(V+C) regressions when iterating networkx nodes
**Learning:** Repeatedly evaluating `nx.simple_cycles()` unconditionally for each node while searching for shell company activity creates a severe regression when processing dense graphs because the cycles generator function is expensive and redundant.
**Action:** Caching the expensive graph operation result lazily via `cycles = None; if cycles is None: cycles = list(nx.simple_cycles(...))` inside the node iteration loops avoids repeating work.
