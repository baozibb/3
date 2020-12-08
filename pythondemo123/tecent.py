#zyx
import requests

url = "https://careers.tencent.com/tencentcareer/api/post/Query?timestamp=1603079775850&countryId=&cityId=&bgIds=&productId=&categoryId=&parentCategoryId=&attrId=&keyword=&pageIndex=1&pageSize=10&language=zh-cn&area=cn"

headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36",
}

def parse_json(url, params={}):
    """解析url，得到字典"""
    response = requests.get(url=url, headers=headers, params=params)
    return response.json()

content = parse_json(url)
print(content)
print(type(content))