from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup

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

# 定义要爬取的网站URL
website_url = "https://www.nytimes.com/2023/07/04/business/federal-judge-biden-social-media.html"

# 发送HTTP GET请求并获取网页内容
driver.get(website_url)

# 使用BeautifulSoup解析网页内容
soup = BeautifulSoup(driver.page_source, "html.parser")

# 查找所有p标签中的文本内容
p_tags = soup.find_all("p")
for p in p_tags:
    print(p.get_text())

# 查找h1标签中的文本内容
h1_tags = soup.find_all("h1")
for h1 in h1_tags:
    print(h1.get_text())

# 关闭浏览器驱动
driver.quit()