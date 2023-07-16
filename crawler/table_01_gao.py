import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import pandas as pd

# 发起请求
url = 'https://www.prensaescrita.com/'
response = requests.get(url)

# 解析 HTML 内容
soup = BeautifulSoup(response.text, 'html.parser')

# 找到所有相对链接
links = []
for link in soup.find_all('a'):
    href = link.get('href')
    if href and not href.startswith('http') and not href.startswith('javascript'):  # 只处理相对链接和非 javascript 链接
        absolute_url = urljoin(url, href)  # 转换为完整的 URL
        links.append(absolute_url)

# 将链接保存在 DataFrame 中
data = pd.DataFrame({'Links': links})

# 发起请求并解析链接内容
dataframe1 = pd.DataFrame()  # 创建空的 DataFrame 存储内容
for link in links:
    if link.startswith('http') or link.startswith('https'):  # 只处理 HTTP/HTTPS 链接
        response = requests.get(link)
        soup = BeautifulSoup(response.text, 'html.parser')

        # 查找具有特定宽度的 <td> 元素
        tds = soup.find_all("td", attrs={"width": ["150", "94", "162"]})

        # 初始化列表以存储内容
        width_150_content = []
        width_94_content = []
        width_162_content = []

        # 提取内容并添加到相应的列表中
        for td in tds:
            width = td.get('width')
            content = td.text.strip()
            if width == "150":
                width_150_content.append(content)
            elif width == "94":
                width_94_content.append(content)
            elif width == "162":
                width_162_content.append(content)

        # 将内容添加到 DataFrame 中
        df = pd.DataFrame({
            'Width 150': width_150_content,
            'Width 94': width_94_content,
            'Width 162': width_162_content
        })

        # 将每个链接的内容 DataFrame 连接到主 DataFrame
        dataframe1 = pd.concat([dataframe1, df], ignore_index=True)

# 保存链接 DataFrame
links_file_path = os.path.join(os.getcwd(), 'links.xlsx')
data.to_excel(links_file_path, index=False)

# 保存内容 DataFrame
content_file_path = os.path.join(os.getcwd(), 'content.xlsx')
dataframe1.to_excel(content_file_path, index=False)

print(f"Data saved to Excel files:\nLinks: {links_file_path}\nContent: {content_file_path}")
