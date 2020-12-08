#zyx
import requests
from lxml import etree
type_url = "https://movie.douban.com/chart"

headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36",
}
def parse_url(url):
    """解析url，得到html"""
    response = requests.get(url=url, headers=headers)
    return response.content
def parse_html(html):
    """解析url，得到字典"""
    etree_obj = etree.HTML(html)
    return etree_obj

content = parse_url(type_url)
a=parse_html(content)
print(content.decode('utf-8'))