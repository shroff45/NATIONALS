## 2024-05-26 - Lazy Evaluation of NetworkX Generators
**Learning:** Found that fully materializing graph generators like `nx.all_simple_paths` and `nx.simple_cycles` inside loops was causing potential $O(2^V)$ or $O(V+E)$ regressions in backend analytical services (`financial_service.py`) during dense graph operations.
**Action:** Always wrap limited-output path queries in `itertools.islice` instead of `list(generator)[:N]`, and cache expensive full-graph evaluations (like cycle detection) outside of node iterations when their output can be reused.
