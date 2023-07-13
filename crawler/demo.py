import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

def crawl_links(url):
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
        
        return extracted_links
    else:
        print(f"Request failed with status code {response.status_code}")
        return None

def crawl_sublink(url, index):
    # Call the crawl_links function with the URL
    result = crawl_links(url)
    write_result_to_file(result)

    # Check if the result is not empty and has at least the specified index
    if result and len(result) >= index:
        # Extract the link at the specified index from the result
        sublink = result[index - 1]

        # Create the absolute URL by joining it with the base URL
        absolute_url = url.rstrip('/') + '/' + sublink.lstrip('/')

        # Send a GET request to the sublink
        response = requests.get(absolute_url)

        # Check if the request was successful
        if response.status_code == 200:
            # Parse the HTML content using BeautifulSoup
            soup = BeautifulSoup(response.content, 'html.parser')

            # Perform further processing with the sublink's content
            # ...

            # Example: Get the title of the sublink's page
            title = soup.title.string
            print(f"Crawled sublink: {absolute_url}")
            print(f"Title of the sublink: {title}")
        else:
            print(f"Request failed with status code {response.status_code}")
    else:
        print("No sublink found at the specified index")


def write_result_to_file(result):
    with open("url.txt", "w") as file:
        for link in result:
            file.write(link + "\n")
    print("Result written to url.txt")


# Example usage
url = 'https://www.fao.org/home/en/#collapseSearchBox'
index = 2

print(crawl_links(url))