#zyx
import re
import bs4
from bs4 import BeautifulSoup
import requests
list=[]
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36',
                   'Cookie':'kbzw__Session=0eh4bvskub1ldvl898af3s3td4; kbz_newcookie=1; Hm_lvt_164fe01b1433a19b507595a43bf58262=1605873048,1605873193; kbzw__user_login=7Obd08_P1ebax9aX2cPl2-DZ1ZmcndHV7Ojg6N7bwNOMraqs3JellNXdpZyp0K_I2pWsr6XcmqXH1qyooanNsMeXnKTs3Ny_zYysr6Wbrp-YnaO2uNXQo67f293l4cqooaWSlonO4OHc0OfUlMfJia-aqJ2WuMbOqayKkKLk6eHO0NHZrd_Vpqymr4-jl5ShwLHNucOOls3g4tiYqNXE3-ieibzU6dHjxqauq6aRnpStqamXqpyvgsnC3djl4ZCllKunqJ8.; Hm_lpvt_164fe01b1433a19b507595a43bf58262=1605873293'}

r=requests.get('http://data.10jqka.com.cn/hgt/hgtb/',headers=headers)
r.encoding = r.apparent_encoding
demo=r.text
soup=BeautifulSoup(demo,'lxml')
for tr in soup.tbody.children:
    if isinstance(tr,bs4.element.Tag):
       tt=tr.find('a')
       h=tt.attrs['href']
       g=re.findall(r'(?<=/)\d{6}(?=/)',h)
       list.append(g[0])
print(list)


