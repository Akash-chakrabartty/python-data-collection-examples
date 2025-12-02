from pathlib import Path
import pandas as pd
import sqlite3

DATA_DIR = Path("data")
DATA_DIR.mkdir(exist_ok=True)

def collect_from_sql():
    db_path = DATA_DIR / "students.db"
    conn = sqlite3.connect(db_path)

    # sample data insert
    df = pd.DataFrame({
        "id": [1, 2, 3],
        "name": ["Akash", "Riya", "Sam"],
        "marks": [85, 90, 78]
    })

    df.to_sql("students", conn, if_exists="replace", index=False)

    # read back
    df2 = pd.read_sql("SELECT * FROM students", conn)
    df2.to_csv(DATA_DIR / "students_sql.csv", index=False)

    conn.close()
    print("SQL Data Saved Successfully ✔️")

if __name__ == "__main__":
    collect_from_sql()
