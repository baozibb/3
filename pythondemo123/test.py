#zyx
from lxml import etree
import requests
url='http://lab.scrapyd.cn'
r=requests.get(url)
con=etree.HTML(r.text)
result=etree.tostring(con)
mingyan=con.xpath("//div[@class='quote post']//div[@class='tags']//a[@class='tag']//text()")
for i in mingyan:
 print(i)

