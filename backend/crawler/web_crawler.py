import requests
from bs4 import BeautifulSoup

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
