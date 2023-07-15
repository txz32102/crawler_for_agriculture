from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import time

# 设置Chrome驱动路径
chrome_driver_path = r"C:\Users\高佳豪\Downloads\chromedriver_win32(1)\chromedriver.exe"

# 配置Chrome选项
chrome_options = Options()
chrome_options.add_argument("--headless")

# 创建Chrome驱动服务
driver_service = Service(chrome_driver_path)

# 定义每次请求的等待时间（单位：秒）
wait_time = 5

# 定义要爬取的网站URL
website_url = "https://www.nytimes.com/2023/07/04/business/federal-judge-biden-social-media.html"

# 创建Chrome浏览器驱动对象
driver = webdriver.Chrome(service=driver_service, options=chrome_options)

while True:
    # 发送HTTP GET请求并获取网页内容
    driver.get(website_url)

    # 获取完整的页面源代码
    page_source = driver.page_source

    # 创建BeautifulSoup对象来解析网页内容
    soup = BeautifulSoup(page_source, "html.parser")

    # 查找所有的p标签并输出文本内容
    p_tags = soup.find_all("p")[:3]  # 仅提取前50行的p标签

    for p_tag in p_tags:
        print(p_tag.get_text())

    # 判断是否已经读取完成
    if len(p_tags) < 50:
        break

    # 进行等待，模拟与网站断开连接
    time.sleep(wait_time)

# 关闭浏览器驱动
driver.quit()
