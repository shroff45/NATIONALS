## 2025-04-06 - Single-Pass Graph Processing Optimization
**Learning:** In graph analysis services like `CaseLinkerService`, performing multi-pass iterations with `[n for n, d in subgraph.nodes(data=True) if d.get("type") == "X"]` to filter node types scales poorly ($O(2N)$), especially when repeated for multiple node types.
**Action:** Always combine graph node iterations into a single pass when filtering by node type and applying logic, reducing the algorithmic complexity to $O(N)$ and substantially improving performance for large graphs.
