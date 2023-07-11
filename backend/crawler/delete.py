import os
import sqlite3

# Get the absolute path of the SQLite database file
db_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../db.sqlite3'))

# Connect to the database
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# Delete all rows from the table
cursor.execute("DELETE FROM crawler_crawler")

# Commit the changes and close the connection
conn.commit()
conn.close()
