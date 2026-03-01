## 2024-05-19 - Missing Indexes in Multi-Tenant DBs
**Learning:** Found that filtering on frequently queried columns in multi-tenant architectures without indexes causes massive performance bottlenecks as the DB grows.
**Action:** Always verify indexes exist on columns used for multi-tenant filtering (like `police_station_id`, `status`, etc).

## 2024-05-19 - Memory Leak in Stateful Services
**Learning:** Storing unbounded request data in instance-level dictionaries (`self.reports`) within singleton services causes memory leaks.
**Action:** Refactor backend services to be stateless or use an external caching/storage mechanism instead of holding references indefinitely.
