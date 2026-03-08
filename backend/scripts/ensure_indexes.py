import sqlite3
import os

def ensure_indexes():
    """
    Manually creates missing indexes on the 'cases' table.
    This script is necessary because the application lacks an automated
    database migration tool (like Alembic).
    """

    # Resolve the database path dynamically, falling back to the default `legalos.db`
    # if the env var isn't set.
    db_url = os.environ.get("DATABASE_URL", "sqlite:///./legalos.db")
    if db_url.startswith("sqlite:///"):
        db_path = db_url.replace("sqlite:///", "")
    else:
        print("This script currently only supports SQLite databases.")
        return

    print(f"Connecting to database at: {db_path}")

    if not os.path.exists(db_path):
        print(f"Database file not found at {db_path}. It might not have been created yet.")
        return

    try:
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()

        # Indexes required for the Case model based on app/models/case.py
        indexes = [
            ("ix_cases_complainant_id", "CREATE INDEX IF NOT EXISTS ix_cases_complainant_id ON cases (complainant_id)"),
            ("ix_cases_status", "CREATE INDEX IF NOT EXISTS ix_cases_status ON cases (status)"),
            ("ix_cases_police_station_id", "CREATE INDEX IF NOT EXISTS ix_cases_police_station_id ON cases (police_station_id)"),
            ("ix_cases_created_at", "CREATE INDEX IF NOT EXISTS ix_cases_created_at ON cases (created_at)")
        ]

        for index_name, create_stmt in indexes:
            print(f"Ensuring index: {index_name}")
            cursor.execute(create_stmt)

        conn.commit()
        print("Successfully applied indexes.")

    except sqlite3.Error as e:
        print(f"SQLite error occurred: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        if 'conn' in locals():
            conn.close()

if __name__ == "__main__":
    ensure_indexes()
