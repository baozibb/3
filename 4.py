#zyx
import bs4
from bs4 import BeautifulSoup
import requests
def getStockList(lst,stockURL):
    # 在同花顺网站获取股票编码
    html = getHTMLText(stockURL)
    soup = BeautifulSoup(html,'lxml')
    a = soup.find_all('a')
    for i in a:
        try:
           href = i.attrs['href']
           if re.findall(r'(?<=/)\d{6}(?=/)',href)[0] not in lst:
                lst.append(re.findall(r'(?<=/)\d{6}(?=/)',href)[0])
        except:
            continue
    print(lst) # 股票编码
def getStockInfo(lst,stockURL,fpath):
    for stock in lst:
        # 根据在同花顺网站获取的股票编码+集思录url获取某个股票的具体信息
       url = stockURL + stock;
       html = getHTMLText(url)
       try:
           if html=="":
                continue
           infoDict = {}
           soup = BeautifulSoup(html,'lxml')
           divList = soup.find('div',attrs={'class':'grid data_content'})
           '''count = 0
           mystr = ""
           for div in divList:
               # print(div)
               mystr = mystr + str(div)
               count += 1
               if count >= 8:
                   break
           # 这一部分就是仅获取图片中的那一部分的数据，为什么是8？我是一点一点数字放大打印出来的
           mystr = mystr.replace('<td> </td>', '')# 将代码中的空格替换掉
           mystr = mystr.replace('<td style="width:  20px;"> </td>','') # 同上
           myhtml = BeautifulSoup(mystr,'html.parser')'''

           name = divList.find_all('li',attrs={'class':'active'})[0]
           infoDict.update({'股票名称':name.text.split()})
           keylist = divList.find_all('td')
           keykeylist = []
           for key in keylist:
               strkey = str(key)
               strkey = strkey.replace('\n','')
               match = re.search(r'(?<=\>).*?(?=\<span)',strkey) or re.search(r'(?<=\>).*?(?=\<sup)',strkey)
               # 将<td title="5年平均股息率：-">股息率<sup>TTM</sup><span class="dc">15.066%</span>和
               # <td style="width: 150px;">现价 <span class="dc">5.310</span></td>
               # 将关键字 现价  和 股息率 提取出来
               if match:
                   keykeylist.append(match.group(0).replace(' ','').replace('<sup>TTM</sup>',''))
			# 将关键字中的空格换行，其他没有信息替换掉
           valuelist = divList.find_all('span',attrs={'class':'dc'})

           for i in range(len(valuelist)):
               key = keykeylist[i]
               val = valuelist[i].text
               infoDict[key] = val
           print(infoDict)

           with open(fpath,'a',encoding='utf-8') as f:
               f.write(str(infoDict)+'\n')
       except:
           traceback.print_exc()
           continue
def getHTMLText(url):
    try:
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36',
                   'Cookie':'kbzw__Session=0eh4bvskub1ldvl898af3s3td4; kbz_newcookie=1; Hm_lvt_164fe01b1433a19b507595a43bf58262=1605873048,1605873193; kbzw__user_login=7Obd08_P1ebax9aX2cPl2-DZ1ZmcndHV7Ojg6N7bwNOMraqs3JellNXdpZyp0K_I2pWsr6XcmqXH1qyooanNsMeXnKTs3Ny_zYysr6Wbrp-YnaO2uNXQo67f293l4cqooaWSlonO4OHc0OfUlMfJia-aqJ2WuMbOqayKkKLk6eHO0NHZrd_Vpqymr4-jl5ShwLHNucOOls3g4tiYqNXE3-ieibzU6dHjxqauq6aRnpStqamXqpyvgsnC3djl4ZCllKunqJ8.; Hm_lpvt_164fe01b1433a19b507595a43bf58262=1605873293'}
        r = requests.get(url,headers=headers)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return ""


import requests
from bs4 import BeautifulSoup
import traceback
import re
def main():
    stock_list_url_hg = "http://data.10jqka.com.cn/hgt/hgtb/"  #沪股
    stock_info_url = "https://www.jisilu.cn/data/stock/"
    output_file = "F:\\BaiduStockInfo1.txt"
    slist = []
    getStockList(slist,stock_list_url_hg)
    getStockInfo(slist,stock_info_url,output_file)
main()
