import os
import sqlite3

# Database file path
file_path = os.path.join(os.path.dirname(__file__), "../../db.sqlite3")

# Connect to the SQLite database
connection = sqlite3.connect(file_path)

# Create a cursor object to execute SQL queries
cursor = connection.cursor()

# Execute a query to fetch all rows from the crawler_crawler table
cursor.execute("SELECT * FROM crawler_crawler")

# Fetch all rows
rows = cursor.fetchall()

# Iterate over the rows
for row in rows:
    # Get the row data
    row_id, url, keyword, tags = row

    # Do something with the row data
    print(f"Row ID: {row_id}")
    print(f"URL: {url}")
    print(f"Keyword: {keyword}")
    print(f"Tags: {tags}")
    print()

# Close the connection
connection.close()
