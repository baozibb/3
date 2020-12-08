#zyx
import requests
url = 'https://careers.tencent.com/tencentcareer/api/post/Query'

headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36",
}

params = {'area': ' cn',
          'attrId': ' ',
          'bgIds': ' ',
          'categoryId': ' ',
          'cityId': ' ',
          'countryId': ' ',
          'keyword': ' ',
          'language': ' zh-cn',
          'pageIndex': ' 1',
          'pageSize': ' 10',
          'parentCategoryId': ' ',
          'productId': ' ',
          'timestamp': ' 1602211262824'}


def parse_json(url, params={}):
    """解析url，得到字典"""
    response = requests.get(url=url, headers=headers, params=params)
    return response.json()


def start():
    for i in range(1, 20):
        params["pageIndex"] = i
        data=parse_json(url, params)
        print(data)
if __name__ == '__main__':
    start()
