import requests
from bs4 import BeautifulSoup

def extract_php_href_attributes(url):
    # Send a GET request to the URL
    response = requests.get(url)

    # Parse the HTML content
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find all tags and extract the href attributes ending with "/filename.php"
    hrefs = []
    for tag in soup.find_all(href=True):
        href = tag.get('href')
        if href and href.endswith(".php") and href.count("/") == 2:
            hrefs.append(href)

    return hrefs

def add_prefix(hrefs, prefix):
    # Add prefix to each href
    prefixed_hrefs = [prefix + href for href in hrefs]

    return prefixed_hrefs

# Example usage
url = 'https://www.prensaescrita.com/'
php_hrefs = extract_php_href_attributes(url)

# Add prefix to the hrefs
prefixed_hrefs = add_prefix(php_hrefs, 'https://www.prensaescrita.com')

# Print the prefixed hrefs
for href in prefixed_hrefs:
    print(href)
