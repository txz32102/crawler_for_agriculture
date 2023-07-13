import re
import requests
from requests import Response
from bs4 import BeautifulSoup
def is_http_url(s):
    regex = re.compile(
        r'^(?:http|ftp)s?://'  # http:// or https://
        r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|'  # domain...
        r'localhost|'  # localhost...
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'  # ...or ip
        r'(?::\d+)?'  # optional port
        r'(?:/?|[/?]\S+)$', re.IGNORECASE)
    if regex.match(s):
        return True
    else:
        return False
url = 'http://www.emol.com/'
#      https://www.trade.gov/country-commercial-guides/chile-agricultural-sector

response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
hii=str(response.headers)
print(hii[10:39])
#print((response.headers)[0:18])
#data = re.findall(r'\d{2}\-\w{3}\-\d{4} \d{2}\:\d{2}',requests.get(url)) #[0]
#hi=requests.Response.headers['Last-Modified']
#print(hi)
# Get the title of the page
title = soup.title.text
print('Title:', title)
#print(response) #.text
# Get all the paragraph text
paragraphs = soup.find_all('p')
#for p in paragraphs:
#    print(p.text)

# Get all the links in the page
mhref = re.compile(r'a.*href="(.*?)"')
mtitle = re.compile(r'<a.* target="_blank">(.*?)</a>')
links = soup.find_all('a')
for link in links:
    href = str(link.get('href'))
    if not is_http_url(href):
        continue
    #mSelf=link.get('_self')
    #h = re.findall(href, str(link))
    title = re.findall(mtitle, str(link))
    if href and '#' not in href:   #'https://www.fao.org' in href or 'http' not in
        print('Link:', href,end='')
        twice=False
        if title:
            if 'img' not in title:
                print(title)   #there is a title
            else:
                twice=True
        else:   #if there is no title
            twice=True
        if twice:
            print('twice',href)
            response2 = requests.get(href)
            soup = BeautifulSoup(response2.text, 'html.parser')
            title = soup.title.text
            print('Title:', title,end='')
            hii = str(response2.headers)
            #print(',hi ', hii[10:39])
            print(hii)
import requests
from bs4 import BeautifulSoup

#url = "https://www.trade.gov/country-commercial-guides/chile-agricultural-sector"
keyword = "agricultural"

# Send a GET request to the URL and get the HTML content
#response = requests.get(url)
html_content = response.content

# Parse the HTML content using BeautifulSoup
#soup = BeautifulSoup(html_content, 'html.parser')

# Find all the tags containing the keyword
tags_containing_keyword = soup.find_all(text=lambda text: text and keyword in text)

# Print the tag and content of each matching tag
#for tag in tags_containing_keyword:
#    print(tag.parent.name)
#    print(tag)
#    print('---')