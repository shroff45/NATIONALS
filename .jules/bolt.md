## 2024-03-20 - Missing Indexes on Case Model
**Learning:** Found critical missing indexes on frequently filtered columns (`status`, `police_station_id`, `created_at`, and `complainant_id`) in `Case` model (`backend/app/models/case.py`) causing full table scans and performance bottlenecks during multi-tenant filtering.
**Action:** Always check models for missing indexes on frequently queried fields, especially in multi-tenant architectures.
