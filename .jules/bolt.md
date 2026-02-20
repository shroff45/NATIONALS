## 2026-02-20 - [Missing Indexes on Core Filters]
**Learning:** The `Case` model lacked database indexes on `status`, `police_station_id`, and `complainant_id`, which are the primary filtering criteria for most views.
**Action:** Always verify indexing on frequently filtered fields in core models like `Case` and `User` to prevent O(n) scan performance degradation as data grows.
