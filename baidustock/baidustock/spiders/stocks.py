import scrapy
import re
class StocksSpider(scrapy.Spider):
    name = 'stocks'
    allowed_domains = ['eastmoney.com']
    start_urls = ['http://eastmoney.com/']

    def parse(self, response):
        pass
