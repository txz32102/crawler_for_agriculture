import requests
from bs4 import BeautifulSoup

url = "https://www.prensaescrita.com/"
response = requests.get(url)

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(response.content, "html.parser")

# Find the <td> tag with the specified attributes
td_tag = soup.find("td", valign="top", align="left")

# Extract the content within the <td> tag
if td_tag:
    content = td_tag.get_text()
    print(content)
else:
    print("No <td> tag found with the specified attributes.")
