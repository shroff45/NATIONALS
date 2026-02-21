## 2024-05-22 - Missing Indexes on Critical Filter Columns
**Learning:** In multi-tenant case management systems, `status` and `location_id` (e.g., `police_station_id`) are the most frequently filtered columns. Defaulting to no index on these columns causes full table scans on every dashboard load.
**Action:** always audit `WHERE` clauses in dashboard queries and ensure corresponding columns are indexed.
