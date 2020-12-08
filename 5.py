#zyx
import re
import bs4
from bs4 import BeautifulSoup
import requests
import traceback
def gethtmltext(url):
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36',
            'Cookie': 'kbzw__Session=0eh4bvskub1ldvl898af3s3td4; kbz_newcookie=1; Hm_lvt_164fe01b1433a19b507595a43bf58262=1605873048,1605873193; kbzw__user_login=7Obd08_P1ebax9aX2cPl2-DZ1ZmcndHV7Ojg6N7bwNOMraqs3JellNXdpZyp0K_I2pWsr6XcmqXH1qyooanNsMeXnKTs3Ny_zYysr6Wbrp-YnaO2uNXQo67f293l4cqooaWSlonO4OHc0OfUlMfJia-aqJ2WuMbOqayKkKLk6eHO0NHZrd_Vpqymr4-jl5ShwLHNucOOls3g4tiYqNXE3-ieibzU6dHjxqauq6aRnpStqamXqpyvgsnC3djl4ZCllKunqJ8.; Hm_lpvt_164fe01b1433a19b507595a43bf58262=1605873293'}

        r = requests.get(url, headers=headers)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return ''
def getstocklist(list,stockurl):
    demo=gethtmltext(stockurl)
    soup=BeautifulSoup(demo,'lxml')
    for tr in soup.tbody.children:
        if isinstance(tr, bs4.element.Tag):
            tt = tr.find('a')
            h = tt.attrs['href']
            g = re.findall(r'(?<=/)\d{6}(?=/)', h)
            list.append(g[0])
    print(list)

def getstockinfo(list,stockurl,fpath):
    for stock in list:
        url=stockurl+str(stock)
        demo=gethtmltext(url)
        try:
            if demo=='':
                print('kong')
                continue
            soup = BeautifulSoup(demo, 'lxml')
            list = soup.find('div', attrs={'class': 'grid data_content'})
            name = list.find('li', attrs={'class': 'active'})
            infodict = {}
            infodict.update({'股票名称': name.text.split()})
            kklist = []
            klist = list.find_all('td')
            for kk in klist:
                strkk = str(kk)
                strkk = strkk.replace('\n', '')
                match = re.search(r'(?<=\>).*?(?=\<span)', strkk) or re.search(r'(?<=\>).*?(?=\<sup)', strkk)
                if match:
                    kklist.append(match.group(0).replace(' ', '').replace('<sup>TTM</sup>', ''))

            vlist = []
            vlist = list.find_all('span', attrs={'class': 'dc'})

            for i in range(len(vlist)):
                key = kklist[i]
                val = vlist[i].text
                infodict[key] = val
            print(infodict)

            with open(fpath,'a',encoding='utf-8')as f:
                f.write(str(infodict)+'\n')

        except:
            traceback.print_exc()
            continue
def main():
    stock_list_url_hg = "http://data.10jqka.com.cn/hgt/hgtb/"  #沪股
    stock_info_url = "https://www.jisilu.cn/data/stock/"
    output_file = "F:\\BaiduStockInfo1.txt"
    slist = []
    getstocklist(slist,stock_list_url_hg)
    getstockinfo(slist,stock_info_url,output_file)
main()