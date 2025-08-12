import requests
from bs4 import BeautifulSoup

def fetch_url(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.text
    else:
        return None

def parse_content(html):
    soup = BeautifulSoup(html, 'html.parser')
    # 假设我们要提取所有的段落文本
    print(soup)
    paragraphs = soup.find_all('p')
    for p in paragraphs:
        print(p.get_text())

url = 'https://aiapps.onepark.com.cn:18080/signin'  # 替换为你想爬取的网址
html_content = fetch_url(url)
if html_content:
    parse_content(html_content)
else:
    print("Failed to fetch URL")