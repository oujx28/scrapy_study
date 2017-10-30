# -*- coding: utf-8 -*-
import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor


class BookSpider(CrawlSpider):
    name = 'book'
    allowed_domains = ['douban.com']
    start_urls = ['https://book.douban.com/tag/']

    rules = [
        #Rule(LinkExtractor(allow=("/subject/\d+$")), callback='parse_subjet'),
        Rule(LinkExtractor(allow='/tag/[^/]+$'), follow=True),
    ]

    # def parse(self, response):
    #     print(response.url)
    #     with open('body.html', 'wb') as f:
    #         f.write(response.body)

    def parse_subjet(self, response):
        print('*********' + response.url)

    def process_request(self, request):
        print(request)


