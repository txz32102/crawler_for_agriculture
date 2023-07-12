from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

# 设置Chrome驱动路径
chrome_driver_path = r"C:\Users\高佳豪\Downloads\chromedriver_win32(1)\chromedriver.exe"

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

# 获取完整的页面源代码
page_source = driver.page_source

# 将页面源代码保存到文件
file_path = r"C:\Users\高佳豪\Desktop\2.html"
with open(file_path, "w", encoding="utf-8") as file:
    file.write(page_source)

from bs4 import BeautifulSoup
# 打开本地HTML文件
local_html_path = r"C:\Users\高佳豪\Desktop\2.html"
with open(local_html_path, "r", encoding="utf-8") as file:
    html_content = file.read()

# 使用BeautifulSoup解析HTML内容
soup = BeautifulSoup(html_content, "html.parser")

# 查找所有的p标签并输出文本内容
p_tags = soup.find_all("p")
for p_tag in p_tags:
    print(p_tag.get_text())
# 关闭浏览器驱动
driver.quit()



