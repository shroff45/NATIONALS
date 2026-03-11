
## 2024-03-12 - [O(N * C) Graph algorithms in node loops]
**Learning:** Calling exponential/factorial graph pathfinding algorithms (like `nx.simple_cycles` which is O((V+E)*C)) inside a node iteration loop `for node in graph.nodes():` creates an O(N * (V+E) * C) bottleneck, which completely breaks and hangs on dense transaction graphs. Also, calling `list()` on a generator of a combinatorial problem causes infinite memory expansion and hanging.
**Action:** Always extract pathfinding or component discovery (like `nx.strongly_connected_components` which is O(V+E)) outside of node loops to evaluate the graph globally, and use lazily evaluated generators with bounds checking instead of eager `list()` evaluations for problems with combinatorial complexity.
