## 2025-02-12 - CI Triage Boundaries
**Learning:** Even when implicitly tasked with resolving CI failures alongside performance optimizations, strict negative constraints (e.g., "Never modify package.json without instruction") must be strictly obeyed. Modifying package.json to fix a CI error when instructed not to modify it is considered a violation.
**Action:** When fixing CI pipelines, find solutions that do not require modifying constrained files, or stop and ask for instruction using `request_user_input` if modifying the constrained file is the only possible solution.
