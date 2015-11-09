# -*- coding: utf-8 -*-
import scrapy


class MydomianSpider(scrapy.Spider):
    name = "mydomian"
    allowed_domains = ["6vhao.com"]
    start_urls = (
        'http://www.6vhao.com/',
    )

    def parse(self, response):
        pass
