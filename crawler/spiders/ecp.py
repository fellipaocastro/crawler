# coding: utf-8

import scrapy

from crawler.items import EcpItem


class EcpSpider(scrapy.Spider):
    name = "ecp"
    allowed_domains = ["epocacosmeticos.com.br"]
    start_urls = ["http://www.epocacosmeticos.com.br/marcas"]

    def parse(self, response):
        self.log("parse: %s" % response.url)
        for sel in response.css('#marcas > div > .menu-departamento > \
.brandFilter > ul > li > a'):
            yield scrapy.Request(
                sel.xpath('@href').extract()[0],
                callback=self.parse_brand
            )

    def parse_brand(self, response):
        self.log("parse_brand %s" % response.url)
        for sel in response.css('h3 > a[href$="/p"]'):
            yield scrapy.Request(
                sel.xpath('@href').extract()[0],
                callback=self.parse_product
            )

    def parse_product(self, response):
        self.log("parse_product %s" % response.url)
        item = EcpItem()
        item['name'] = response.css('div.productName[itemprop="name"]::text')\
            .extract()
        item['title'] = response.css('title::text').extract()
        item['url'] = response.url
        yield item
