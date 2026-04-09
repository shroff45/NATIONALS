## 2024-05-18 - [Optimizing Graph Node Pattern Detection]
**Learning:** The `_detect_patterns` method in `backend/app/services/case_linker_service.py` was originally iterating over `subgraph.nodes` multiple times via list comprehensions to filter out specific node types ("Suspect" and "MO") before processing them. This is an $O(2V)$ anti-pattern for graph traversal.
**Action:** Always look for opportunities to combine multi-pass graph node iterations into a single-pass $O(V)$ loop when filtering multiple node attributes, reducing memory allocations for intermediate list comprehensions.
