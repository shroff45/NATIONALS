## 2024-05-23 - Database Schema Management
**Learning:** The backend lacks automated database migrations (e.g., Alembic). Schema changes are applied by deleting the SQLite database file and letting the application recreate it on startup.
**Action:** When modifying models, always verify schema changes using a fresh database instance (e.g., a temporary test DB) or by explicitly recreating the main database. Do not assume existing databases will be updated automatically.

## 2024-05-23 - SQLite Artifacts
**Learning:** SQLite generates `*-shm` (Shared Memory) and `*-wal` (Write-Ahead Log) files during runtime. These are binary temporary files that contain volatile database state.
**Action:** Ensure these files (`*.db-shm`, `*.db-wal`) are added to `.gitignore` and never committed to version control, as they can cause conflicts and corrupt the database state for other developers.
