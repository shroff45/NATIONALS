## 2024-05-24 - Missing Indexes in Case Model
**Learning:** The `Case` model lacked database indexes on `status`, `police_station_id`, and `created_at`, which are critical for filtering and sorting in list views. Even with small datasets (10k records), adding indexes reduced query time by ~33% (from 6ms to 4ms) and changed complexity from O(N) to O(log N).
**Action:** Always check `WHERE` and `ORDER BY` clauses in API endpoints and ensure corresponding columns are indexed in the SQLAlchemy model.
