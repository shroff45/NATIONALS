## 2025-03-07 - [Missing Indexes in Multi-Tenant Architecture]
**Learning:** Found critical missing database indexes on frequently filtered columns (`status`, `police_station_id`, `complainant_id`, `created_at`) in `Case` model. In a multi-tenant application, missing indexes on tenant IDs (`police_station_id`, `complainant_id`) and common filter/sort fields causes full table scans, degrading performance.
**Action:** Always verify indexes exist on foreign keys, tenant identifiers, and commonly queried fields like `status` or `created_at`. Ensure to follow codebase convention: add comments explaining the specific business use case when adding database indexes.

## 2025-03-07 - [Unbounded Dictionaries in Singleton Services]
**Learning:** Found multiple Singleton backend services (`BailReckonerService`, `SentencingAssistantService`, `JudgmentValidatorService`) using unbounded `self.reports = {}` dictionaries to store reports in-memory indefinitely. This leads to a memory leak in a long-running process as the dictionary grows forever with every request.
**Action:** Replace `self.reports = {}` with a bounded FIFO structure (e.g., using `self.reports.pop(next(iter(self.reports)))` capped at 1000 items) to prevent memory leaks in production.
