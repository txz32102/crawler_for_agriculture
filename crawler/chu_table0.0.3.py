import requests
from bs4 import BeautifulSoup
import pandas as pd
import os

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

class TableCrawler:
    def __init__(self, url):
        self.url = url

    def crawl_and_get_content(self):
        # Send a GET request to the URL
        response = requests.get(self.url)

        # Parse the HTML content
        soup = BeautifulSoup(response.content, "html.parser")

        # Find all <td> elements with specific widths
        tds = soup.find_all("td", attrs={"width": ["150", "94", "162"]})

        # Initialize lists to store the content
        width_150_content = []
        width_94_content = []
        width_162_content = []

        # Extract the content based on the width
        for td in tds:
            width = td["width"]
            content = td.get_text(strip=True)

            if width == "150":
                width_150_content.append(content)
            elif width == "94":
                strong_element = td.find("strong")
                if strong_element:
                    width_94_content.append(strong_element.get_text(strip=True))
            elif width == "162":
                a_element = td.find("a")
                if a_element:
                    width_162_content.append(a_element["href"])

        return width_150_content, width_94_content, width_162_content

    def combine_to_dataframe(self):
        # Get the extracted content
        width_150_content, width_94_content, width_162_content = self.crawl_and_get_content()

        # Create a DataFrame
        data = {
            "Width 150": width_150_content,
            "Width 94": width_94_content,
            "Width 162": width_162_content
        }
        df = pd.DataFrame(data)

        return df



url = "https://www.prensaescrita.com/america/chile.php"
url_list = extract_php_href_attributes(url)
url_list = add_prefix(url_list, "https://www.prensaescrita.com")


i = 0
for url in url_list:
    print(i)
    print(url)
    filename = url.replace("/", "_")  # Substitute '/' with '_'
    crawler = TableCrawler(url)
    df = crawler.combine_to_dataframe()
    print(df)
    i = i + 1

url = ''
crawler = TableCrawler(url)
