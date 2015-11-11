#coding=utf-8

from scrapy.selector import HtmlXPathSelector
import scrapy
import os

class PageSpider(scrapy.Spider):
    name = "PageSpider"
    allowed_domains = ["jandan.net/ooxx"]
    if not os.path.exists('./htmls'):
        os.mkdir('./htmls')

    start_urls = []
    for page in range(1400, 1450):
        start_urls.append('http://jandan.net/ooxx/page-%d' % page)

    print "---------urls---------"
    print start_urls
    def parse(self, response):
        hxs = HtmlXPathSelector(response)
        filename = hxs.select("//span[@class='current-comment-page']/text()").extract()[0] + ".html"
        open('./htmls/' + filename, 'wb').write(response.body)
        pass
