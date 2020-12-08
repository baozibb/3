#zyx
from scrapy.selector import Selector
import requests
url='http://lab.scrapyd.cn'
r=requests.get(url)
#print(r.text)
selector = Selector(text=r.text)
print(Soup.select(''))