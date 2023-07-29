import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
import pandas as pd
import concurrent.futures

# 定义函数来爬取链接中的所有h2标签内容
def crawl_h2_tags(link):
    if pd.notna(link):  # 检查链接是否是非空值
        if not link.startswith('http'):  # 补充缺失的协议部分
            link = 'http://' + link
        parsed_url = urlparse(link)
        if parsed_url.scheme not in ['http', 'https']:
            print(f"Invalid URL format: {link}")
            return []
        try:
            response = requests.get(link, timeout=10)  # 设置较长的超时时间
            response.raise_for_status()  # 检查是否请求成功，如果失败会抛出异常
            soup = BeautifulSoup(response.text, 'html.parser')
            h2_tags = soup.find_all('h2')
            return [tag.get_text() for tag in h2_tags]
        except requests.exceptions.RequestException as e:
            print(f"Error occurred while crawling {link}: {e}")
            return []
        except Exception as e:
            print(f"Error occurred while processing {link}: {e}")
            return []
    else:
        return []  # 如果链接为空值，返回空列表

# 定义函数来爬取链接内容
def crawl_link(link):
    if link.startswith('http') or link.startswith('https'):
        try:
            response = requests.get(link, timeout=10)
            response.raise_for_status()
            return response
        except requests.exceptions.RequestException as e:
            print(f"Error occurred while crawling {link}: {e}")
            return None
    else:
        return None

# 发起请求
url = 'https://www.prensaescrita.com/'
response = requests.get(url)

# 解析 HTML 内容
soup = BeautifulSoup(response.text, 'html.parser')

# 找到当前页面的链接
current_page_link = url

# 找到所有相对链接
links = [current_page_link]  # 将当前页面链接添加到链接列表

for link in soup.find_all('a'):
    href = link.get('href')
    if href and not href.startswith('http') and not href.startswith('javascript'):
        # 只处理相对链接和非 javascript 链接
        absolute_url = urljoin(url, href)  # 转换为完整的 URL
        links.append(absolute_url)

# 使用 ThreadPoolExecutor 进行多线程爬取链接内容
with concurrent.futures.ThreadPoolExecutor(max_workers=25) as executor:
    future_to_link = {executor.submit(crawl_link, link): link for link in links}

    dataframe1 = pd.DataFrame()  # 创建空的 DataFrame 存储内容

    for future in concurrent.futures.as_completed(future_to_link):
        link = future_to_link[future]
        try:
            response = future.result()
            if response:
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

                # 检查所有列表是否具有相同的长度
                min_length = min(len(width_150_content), len(width_94_content), len(width_162_content))

                # 将内容添加到 DataFrame 中
                df = pd.DataFrame({
                    'Width 150': width_150_content[:min_length],
                    'Width 94': width_94_content[:min_length],
                    'Width 162': width_162_content[:min_length],
                    'Link': [link] * min_length
                })

                # 将每个链接的内容 DataFrame 连接到主 DataFrame
                dataframe1 = pd.concat([dataframe1, df], ignore_index=True)

        except Exception as e:
            print(f"Error occurred while processing {link}: {e}")

# 使用 ThreadPoolExecutor 进行多线程爬取 Width 162 中的 h2 标签内容
with concurrent.futures.ThreadPoolExecutor(max_workers=25) as executor:
    future_to_h2_tags = {executor.submit(crawl_h2_tags, link): link for link in dataframe1['Width 162']}

    for future in concurrent.futures.as_completed(future_to_h2_tags):
        link = future_to_h2_tags[future]
        try:
            h2_tags = future.result()
            # 将 h2_tags 结果添加到对应行中
            index = dataframe1[dataframe1['Width 162'] == link].index[0]
            dataframe1.at[index, 'H2 Tags'] = h2_tags

        except Exception as e:
            print(f"Error occurred while processing {link}: {e}")

# 过滤出H2 Tags中包含"Tele"的行
keyword = "Tele"  # 设置关键字
filtered_dataframe = dataframe1[dataframe1['H2 Tags'].apply(lambda x: isinstance(x, list) and any(keyword in tag for tag in x))]

# 输出结果
print(filtered_dataframe)

# 保存结果到Excel文件
filtered_dataframe.to_excel('data1.xlsx', index=False)  # 将DataFrame保存到data1.xlsx
