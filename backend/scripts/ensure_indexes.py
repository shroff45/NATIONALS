import sqlite3
import os

DB_PATH = os.path.join(os.path.dirname(__file__), "..", "legalos.db")

def ensure_indexes():
    """Manually apply indexes to the SQLite database without Alembic."""
    if not os.path.exists(DB_PATH):
        print(f"Database {DB_PATH} not found. Indexes will be created automatically on next init.")
        return

    print(f"Connecting to {DB_PATH}...")
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    indexes_to_create = [
        ("ix_cases_complainant_id", "cases", "complainant_id"),
        ("ix_cases_status", "cases", "status"),
        ("ix_cases_police_station_id", "cases", "police_station_id"),
        ("ix_cases_created_at", "cases", "created_at"),
    ]

    for idx_name, table, column in indexes_to_create:
        try:
            cursor.execute(f"CREATE INDEX IF NOT EXISTS {idx_name} ON {table} ({column})")
            print(f"Ensured index {idx_name} on {table}({column})")
        except sqlite3.Error as e:
            print(f"Error creating index {idx_name}: {e}")

    conn.commit()
    conn.close()
    print("Finished ensuring indexes.")

if __name__ == "__main__":
    ensure_indexes()
