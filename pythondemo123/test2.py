#zyx
import json
import redis
import requests

s=requests.session()
s.headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:73.0) Gecko/20100101 Firefox/73.0'}
page=s.get('https://feed.sina.com.cn/api/roll/get?pageid=121&lid=1356&num=20&versionNumber=1.2.4&page=2&encode=utf-8')
print((json.loads(page.content.decode("utf-8"))))