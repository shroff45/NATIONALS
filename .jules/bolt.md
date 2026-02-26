## 2024-05-23 - [Missing Core Indexes]
**Learning:** Found critical missing indexes on `Case` model for `created_at` and `police_station_id`. These fields are frequently used for sorting and filtering in dashboards.
**Action:** Added `index=True` to `status`, `police_station_id`, `created_at`, and `complainant_id`. Sorting by date improved by ~82% (0.0039s -> 0.0007s). Filtering by station improved by ~28% (0.0081s -> 0.0058s).
