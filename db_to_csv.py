import sqlite3
import pandas as pd

db_file = "./data.db"

conn = sqlite3.connect(db_file, isolation_level=None, detect_types=sqlite3.PARSE_COLNAMES)
db_df = pd.read_sql_query("SELECT * FROM syllabi", conn)
db_df.to_csv('syllabi.csv', index=False)