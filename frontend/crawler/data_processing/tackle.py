import os
import sqlite3
import requests
from bs4 import BeautifulSoup

# Function to crawl the keyword in a URL and extract tags
def crawl_keyword(url, keyword):
    # Send a GET request to the URL
    response = requests.get(url)

    # Parse the HTML content
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find all tags that contain the keyword
    tags = soup.find_all(string=lambda text: text and keyword in text)

    # Return the tags as a string separated by commas
    return ', '.join(tags)

# Function to update the tags in the database
def update_tags(row_id, updated_tags):
    # Connect to the SQLite database
    connection = sqlite3.connect(file_path)

    # Create a cursor object to execute SQL queries
    cursor = connection.cursor()

    # Execute an SQL update query to update the tags for the corresponding row
    cursor.execute("UPDATE crawler_crawler SET tags = ? WHERE id = ?", (updated_tags, row_id))

    # Commit the changes to the database
    connection.commit()

    # Close the connection
    connection.close()

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

    # Crawl the keyword in the URL and get the updated tags
    updated_tags = crawl_keyword(url, keyword)

    # If no keyword found, update the tags with a message
    if not updated_tags:
        updated_tags = f"%{keyword} is not in website {url}%"

    # Update the tags in the database
    update_tags(row_id, updated_tags)

# Close the connection
connection.close()
