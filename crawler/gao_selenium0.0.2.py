import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

# 定义要爬取的网站URL
website_url = "https://www.prensaescrita.com/"

# 设置Chrome驱动路径
chrome_driver_path = r"C:\Users\高佳豪\Downloads\chromedriver_win32(1)\chromedriver.exe"
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

# 遍历每个链接（包括a标签和frame标签）
for link in links + frames:
    # 获取链接的URL
    url = link.get("href") or link.get("src")

    # 检查链接是否为空
    if url is not None:
        # 添加默认协议（https）
        if not url.startswith("http"):
            url = urljoin(website_url, url)

        print(url)

# 关闭浏览器驱动
driver.quit()