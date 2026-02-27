import sqlite3
import os

def create_index_safely(cursor, table, column, index_name):
    print(f"Checking index {index_name} on {table}.{column}...")
    try:
        cursor.execute(f"CREATE INDEX IF NOT EXISTS {index_name} ON {table} ({column})")
        print(f"Verified/Created index {index_name}.")
    except sqlite3.Error as e:
        print(f"Error creating index {index_name}: {e}")

def main():
    db_path = "legalos.db"

    if not os.path.exists(db_path):
        print(f"Database file {db_path} not found. Skipping migration.")
        return

    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    indexes_to_add = [
        ("cases", "status", "ix_cases_status"),
        ("cases", "police_station_id", "ix_cases_police_station_id"),
        ("cases", "created_at", "ix_cases_created_at"),
        ("cases", "complainant_id", "ix_cases_complainant_id"),
        ("cases", "fir_number", "ix_cases_fir_number")
    ]

    for table, column, index_name in indexes_to_add:
        create_index_safely(cursor, table, column, index_name)

    conn.commit()
    conn.close()

if __name__ == "__main__":
    main()
