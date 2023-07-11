import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

# 定义关键词
keyword = "agriculture"

# 定义要爬取的网站URL
website_url = "https://www.fao.org"

# 设置Chrome驱动路径
chrome_driver_path = r"/home/musong/.local/lib/python3.10/site-packages/chromedriver_binary/chromedriver"

# 配置Chrome选项
chrome_options = Options()
chrome_options.add_argument("--headless") 

# 创建Chrome驱动服务
driver_service = Service(chrome_driver_path)

# 创建Chrome浏览器驱动对象
driver = webdriver.Chrome(service=driver_service, options=chrome_options)

# 设置超时时间（单位：秒）
timeout = 30

# 发送HTTP GET请求并获取网页内容
driver.get(website_url)

# 创建BeautifulSoup对象来解析网页内容
soup = BeautifulSoup(driver.page_source, "html.parser")

# 提取所有链接（a标签和frame标签的src属性）
links = soup.find_all("a")
frames = soup.find_all("iframe")

# 用于存储已打印链接的集合
printed_links = set()

# 遍历每个链接（包括a标签和frame标签）
for link in links + frames:
    # 获取链接的URL
    url = link.get("href") or link.get("src")

    # 检查链接是否为空
    if url is not None:
        # 添加默认协议（https）
        if not url.startswith("http"):
            url = urljoin(website_url, url)

        try:
            # 切换到frame
            if link.name == "frame":
                driver.switch_to.frame(link)
            else:
                driver.switch_to.default_content()

            # 发送HTTP GET请求并获取链接页面内容，设置超时时间
            link_response = requests.get(url, timeout=timeout)
            link_content = link_response.content

            # 创建链接页面的BeautifulSoup对象
            link_soup = BeautifulSoup(link_content, "html.parser")

            # 搜索链接页面内容是否包含关键词
            if keyword in link_soup.get_text():
                # 检查链接是否已经打印过
                if url not in printed_links:
                    print(url)
                    # 将链接添加到已打印链接的集合中
                    printed_links.add(url)
        except requests.exceptions.Timeout:
            print(f"请求链接超时：{url}")
        except requests.exceptions.RequestException as e:
            print(f"请求发生错误：{url}")
            print(e)

# 关闭浏览器驱动
driver.quit()
