import os
import sqlite3
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

DB_PATH = "legalos.db"

def ensure_indexes():
    """Manually add indexes to SQLite database for the cases table."""
    if not os.path.exists(DB_PATH):
        logger.error(f"Database not found at {DB_PATH}. Run the backend app to create it first.")
        return

    logger.info(f"Connecting to database at {DB_PATH}")
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    indexes_to_create = [
        ("ix_cases_complainant_id", "CREATE INDEX IF NOT EXISTS ix_cases_complainant_id ON cases (complainant_id)"),
        ("ix_cases_status", "CREATE INDEX IF NOT EXISTS ix_cases_status ON cases (status)"),
        ("ix_cases_police_station_id", "CREATE INDEX IF NOT EXISTS ix_cases_police_station_id ON cases (police_station_id)"),
        ("ix_cases_created_at", "CREATE INDEX IF NOT EXISTS ix_cases_created_at ON cases (created_at)")
    ]

    for index_name, sql in indexes_to_create:
        try:
            logger.info(f"Executing: {sql}")
            cursor.execute(sql)
            logger.info(f"Successfully created/verified index {index_name}")
        except sqlite3.Error as e:
            logger.error(f"Error creating index {index_name}: {e}")

    conn.commit()
    conn.close()
    logger.info("Database index application complete.")

if __name__ == "__main__":
    ensure_indexes()
