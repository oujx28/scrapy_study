# -*- coding: utf-8 -*-
import scrapy
from scrapy.spiders import Rule, CrawlSpider
from scrapy.linkextractors import LinkExtractor
from ..items import HrtencentItem


class HrSpider(CrawlSpider):
    name = 'hr'
    allowed_domains = ['tencent.com']
    start_urls = ['http://hr.tencent.com/position.php']
    rules = [
        Rule(LinkExtractor(allow="position_detail.php\?id=\d*"), follow=False, callback='parse_detail'),
        Rule(LinkExtractor(allow="position.php\?&start=\d{,2}#a$"), follow=True)
    ]

    def parse_detail(self, response):
        item = HrtencentItem()
        item['title'] = response.css('.sharetitle::text').extract_first()
        item['address'] = response.css(".bottomline td::text").extract_first()
        item['intro'] = response.css('.squareli li::text').extract()
        yield item



