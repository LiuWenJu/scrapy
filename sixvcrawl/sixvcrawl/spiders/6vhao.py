# -*- coding: utf-8 -*-
import scrapy

from sixvcrawl.items import SixvcrawlItem

class A6vhaoSpider(scrapy.Spider):
    name = "6vhao"
    allowed_domains = ["6vhao.com"]
    start_urls = [
        "http://www.6vhao.com/",
        "http://www.6vhao.com/dy/2015-06-26/25556.html",
        "http://www.6vhao.com/dy/2015-06-30/25581.html",
        "http://www.6vhao.com/dy/2015-06-13/25484.html"

    ]

    def parse(self, response):
        for sel in response.xpath('//ul/li'):
            item = SixvcrawlItem()
            item['title'] = sel.xpath('a/text()').extract()
            item['link'] = sel.xpath('a/@href').extract()
            item['desc'] = sel.xpath('text()').extract()
            #print title, link, desc
            yield item


