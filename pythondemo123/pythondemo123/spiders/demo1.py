import scrapy

from protego import Protego
class Demo1Spider(scrapy.Spider):
    name = 'demo1'
    allowed_domains = ['python123.io']
    start_urls = ['http://python123.io/']

    def parse(self, response):

        fname = response.url.split('/')[-1]
        with open(fname, 'wb')as f:
            f.write(response.body)
            self.log('save file %s.' % fname)
        pass
