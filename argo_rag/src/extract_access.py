# src/extract_access.py
import pyodbc

def load_access_data(db_path, limit_per_table=5000):
    """
    Load data from an Access database and return as documents for Chroma.
    
    Args:
        db_path (str): Path to the .accdb file
        limit_per_table (int): Max rows to load per table (None = all rows)
    """
    conn_str = (
        r"DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};"
        f"DBQ={db_path};"
    )
    conn = pyodbc.connect(conn_str)
    cursor = conn.cursor()

    tables = [t.table_name for t in cursor.tables(tableType="TABLE")]
    docs = []

    for table in tables:
        print(f"📑 Reading table: {table}")
        cursor.execute(f"SELECT * FROM {table}")
        columns = [column[0] for column in cursor.description]

        count = 0
        while True:
            rows = cursor.fetchmany(500)  # fetch in chunks
            if not rows:
                break

            for row in rows:
                row_dict = dict(zip(columns, row))
                docs.append({
                    "id": f"{table}_{count}",
                    "text": f"Table: {table}\nRow: {row_dict}"
                })
                count += 1
                if limit_per_table and count >= limit_per_table:
                    break

            if limit_per_table and count >= limit_per_table:
                print(f"⚠️ Reached limit ({limit_per_table}) for table {table}")
                break

        print(f"✔️ Loaded {count} rows from {table}")

    conn.close()
    return docs


if __name__ == "__main__":
    db_path = r"data\ARGO_DB_2004.accdb"
    docs = load_access_data(db_path, limit_per_table=2000)
    print(f"\n✅ Total loaded rows: {len(docs)}")
    print("🔎 Sample:", docs[:2])
