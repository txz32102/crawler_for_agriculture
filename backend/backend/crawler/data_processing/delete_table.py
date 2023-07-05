import os
import sqlite3

# Database file path
file_path = os.path.join(os.path.dirname(__file__), "../../db.sqlite3")

# Connect to the SQLite database
connection = sqlite3.connect(file_path)

# Create a cursor object to execute SQL queries
cursor = connection.cursor()

# Execute a query to delete the crawler_crawler table
cursor.execute("DROP TABLE crawler_crawler")

# Commit the changes to the database
connection.commit()

# Close the connection
connection.close()
