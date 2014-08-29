# coding: utf-8

import scrapy

from crawler.items import EcpItem


class EcpSpider(scrapy.Spider):
    name = "ecp"
    allowed_domains = ["epocacosmeticos.com.br"]
    start_urls = ["http://www.epocacosmeticos.com.br/marcas"]

    def parse(self, response):
        self.log("Visited %s" % response.url)
        for sel in response.css('#marcas > div > .menu-departamento > \
.brandFilter > ul > li > a'):
            return scrapy.Request(
                sel.xpath('@href').extract()[0],
                callback=self.parse_brand
            )

    def parse_brand(self, response):
        self.log("Visited %s" % response.url)
        for sel in response.css('h3 > a[href$="/p"]'):
            item = EcpItem()
            item['name'] = sel.xpath('text()').extract()
            item['title'] = sel.xpath('@title').extract()
            item['url'] = sel.xpath('@href').extract()
            yield item
