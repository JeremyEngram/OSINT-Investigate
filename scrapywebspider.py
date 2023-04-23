import scrapy

class MySpider(scrapy.Spider):
    name = 'example.com'
    allowed_domains = ['example.com']
    start_urls = ['http://www.example.com']

    def parse(self, response):
        # parse HTML page and extract relevant data
        yield {
            'title': response.css('title::text').get(),
            'body': response.css('body::text').get()
        }
