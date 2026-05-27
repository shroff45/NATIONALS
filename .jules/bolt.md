## 2024-05-27 - Lazily evaluate NetworkX paths
**Learning:** In the backend `financial_service.py`, using `list(nx.all_simple_paths(...))` before slicing (e.g., `[:5]`) forces NetworkX to compute all possible simple paths. For dense graphs, this causes exponential $O(V!)$ time and memory consumption, leading to severe performance bottlenecks.
**Action:** Use `itertools.islice(nx.all_simple_paths(...), 5)` to lazily evaluate generators, stopping computation exactly when the required number of paths is found.
