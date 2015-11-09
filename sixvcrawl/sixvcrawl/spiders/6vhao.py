# -*- coding: utf-8 -*-
import scrapy


class A6vhaoSpider(scrapy.Spider):
    name = "6vhao"
    allowed_domains = ["6vhao.com"]
    start_urls = (
        'http://www.6vhao.com/',
    )

    def parse(self, response):
        pass
