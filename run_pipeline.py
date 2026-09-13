"""Rebuild the cleaned dataset, SQLite database, charts, and dashboard.

Run from the project directory with:
    python run_pipeline.py
"""

from pathlib import Path
import sqlite3
import subprocess
import sys

import pandas as pd


ROOT = Path(__file__).resolve().parent


def main():
    subprocess.run([sys.executable, str(ROOT / "clean_data.py")], cwd=ROOT, check=True)
    subprocess.run([sys.executable, str(ROOT / "make_charts.py")], cwd=ROOT, check=True)

    clean_path = ROOT / "outputs" / "sales_clean.csv"
    db_path = ROOT / "outputs" / "sales.db"
    frame = pd.read_csv(clean_path)
    with sqlite3.connect(db_path) as connection:
        frame.to_sql("sales", connection, if_exists="replace", index=False)
        connection.execute("CREATE INDEX IF NOT EXISTS idx_sales_order_date ON sales(Order_Date)")
        connection.execute("CREATE INDEX IF NOT EXISTS idx_sales_category ON sales(Category)")
        connection.commit()
    print(f"Rebuilt {len(frame):,} rows in {db_path}")


if __name__ == "__main__":
    main()
