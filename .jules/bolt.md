# Bolt's Journal

## 2024-05-22 - Missing Indexes
**Learning:** SQLite queries on non-indexed columns in  model (status, police_station_id) are causing full table scans.
**Action:** Always add indexes to foreign keys and frequently filtered columns.
