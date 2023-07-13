import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

def crawl_links(url, keyword):
    # Send a GET request to the URL
    response = requests.get(url)
    
    # Check if the request was successful
    if response.status_code == 200:
        # Parse the HTML content using BeautifulSoup
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Find all the <a> tags (links) in the HTML
        links = soup.find_all('a')

        # Create a list to store the extracted links
        extracted_links = []
        
        # Iterate over the links and append their href attribute to the list
        for link in links:
            href = link.get('href')
            
            # Check if the href value is not None
            if href is not None:
                # Check if the href value is a fragment identifier
                if href.startswith('#'):
                    # Skip fragment identifiers
                    continue
                
                # Check if the href value is a relative URL
                if not href.startswith('http'):
                    href = urljoin(url, href)
                
                extracted_links.append(href)
        
        print(extracted_links)
        return extracted_links[1:10]
    else:
        print(f"Request failed with status code {response.status_code}")
        return None

def crawl_keywords(url, keyword):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    tags_with_content = []
    for tag in soup.find_all():
        if keyword in tag.get_text():
            tags_with_content.append(tag.get_text())

    if not tags_with_content:
        error_message = f"{keyword} is not found in {url}"
        return error_message

    return tags_with_content
