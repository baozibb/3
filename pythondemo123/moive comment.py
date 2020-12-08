#zyx
# encoding: utf-8

import requests
import time
import re
import random
import csv
from lxml import etree

type_url = "https://movie.douban.com/chart"
movie_url = "https://movie.douban.com/j/chart/top_list"

headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36",
}


def parse_html(url, params={}):
    """解析url，得到html"""
    response = requests.get(url=url, headers=headers, params=params)
    return response.content.decode("utf-8")


def parse_json(url, params={}):
    """解析url，得到字典"""
    response = requests.get(url=url, headers=headers, params=params)
    return response.json()


def get_movie_type():
    """获取电影分类"""
    content = parse_html(type_url)
    return re.findall(r'<a href="/typerank\?type_name=(.*?)&type=(\d+)&interval_id=100:90&action=">.*?</a>', content)


def get_movie(movie_type, low_score, high_score):
    """获取电影"""
    movie = {
        "title": "",  # 电影名称
        "actors": "",  # 主演
        "release_date": "",  # 上映日期
        "regions": "",  # 上映地
        "types": "",  # 类型
        "score": "",  # 评分
        "vote_count": "",  # 评论数
        "url": "",  # url
    }

    movie_type_name = movie_type[0]
    movie_type_num = movie_type[1]

    i = 0
    while True:
        # 参数
        params = {
            "type": movie_type_num,
            "interval_id": "{}:{}".format(high_score, low_score),
            "action": "",
            "start": i,
            "limit": 20
        }
        # 发请求获取数据
        data_list = parse_json(movie_url, params)
        # 判断循环退出
        if not data_list:
            break
        # 循环
        for data in data_list:
            movie["title"] = data["title"]
            movie["actors"] = data["actors"]
            movie["release_date"] = data["release_date"]
            movie["regions"] = data["regions"]  # 国家
            movie["types"] = data["types"]  # 类型
            movie["score"] = data["score"]  # 评分
            movie["vote_count"] = data["vote_count"]  # 评论条数
            movie["url"] = data["url"]  # url
            save(movie)

        i += 20


def save(item):
    """将数据保存到csv中"""
    with open("./豆瓣电影.csv", "a", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(item.values())


def start():
    """爬虫开始"""
    low_score = int(input("输入要爬取的最低分（以5为单位），最高分默认是加10>"))
    high_score = low_score + 10

    movie_type_list = get_movie_type()
    for movie_type in movie_type_list:
        print("{}爬取中...".format(movie_type[0]))
        get_movie(movie_type, low_score, high_score)


if __name__ == '__main__':
    start()

#  测试代码：
# content = parse_url(type_url)
# # 由于有iframe 所以不能使用xpath
# print(re.findall(r'<a href="/typerank\?type_name=(.*?)&type=(\d+)&interval_id=100:90&action=">.*?</a>',content))
#
#
# """
# <a href="/typerank?type_name=剧情&amp;type=11&amp;interval_id=100:90&amp;action=">剧情</a>
#
# r'<a href="/typerank\?type_name=(.*?)&type=(\d+)&interval_id=100:90&action=">.*?</a>'
# """
#
# response = requests.get(url=movie_url,headers=headers)
# content = response.json()
# print(content)
