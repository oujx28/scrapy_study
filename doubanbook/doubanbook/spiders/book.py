# -*- coding: utf-8 -*-
import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from ..items import DoubanbookItem


class BookSpider(CrawlSpider):
    name = 'book'
    allowed_domains = ['douban.com']
    start_urls = ['https://book.douban.com/tag/']
    #start_urls = ['https://book.douban.com/tag/%E5%B0%8F%E8%AF%B4']

    rules = [
        Rule(LinkExtractor(allow=("/subject/\d+/$")), callback='parse_subjet'),
        Rule(LinkExtractor(allow='/tag/[^/]+$'), follow=True),
    ]

    # def parse(self, response):
    #     print(response.url)
    #     with open('body.html', 'wb') as f:
    #         f.write(response.body)

    def parse_subjet(self, response):
        item = DoubanbookItem()
        item['title'] = response.css('h1 span::text').extract_first()
        item['link'] = response.url
        item['intro'] = response.css('#link-report .intro p::text').extract_first()
        yield item

    def process_request(self, request):
        print(request)


