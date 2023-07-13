from bs4 import BeautifulSoup
from urllib.parse import urljoin
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
}

# 定义要爬取的网站URL
website_url = "https://www.nytimes.com/2023/07/04/business/federal-judge-biden-social-media.html"

# 设置Chrome驱动路径
chrome_driver_path = r"C:\Users\高佳豪\Downloads\chromedriver_win32(1)\chromedriver.exe"
chrome_driver_path = r"/home/musong/.local/lib/python3.10/site-packages/chromedriver_binary/chromedriver"

# 配置Chrome选项
chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument(f"--user-agent={headers['User-Agent']}")

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
        # 检查链接是否是网站内的链接
        if website_url in url:
            # 创建链接页面的BeautifulSoup对象
            link_soup = BeautifulSoup(driver.page_source, "html.parser")

            # 提取链接页面中的所有链接
            inner_links = link_soup.find_all("a")

            # 遍历每个内部链接
            for inner_link in inner_links:
                inner_url = inner_link.get("href")

                # 检查内部链接是否为空
                if inner_url is not None:
                    # 添加默认协议（https）
                    if not inner_url.startswith("http"):
                        inner_url = urljoin(url, inner_url)

                    print(inner_url)

# 关闭浏览器驱动
driver.quit()