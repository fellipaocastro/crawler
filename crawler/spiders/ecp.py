# coding: utf-8

import scrapy

from crawler.items import EcpItem


class EcpSpider(scrapy.Spider):
    name = "ecp"
    allowed_domains = ["epocacosmeticos.com.br"]
    start_urls = ["http://www.epocacosmeticos.com.br/marcas"]

    def parse(self, response):
        # for sel in response.css('h3 > a[href$="/p"]'):
        #     item = EcpItem()
        #     item['name'] = sel.xpath('text()').extract()
        #     item['title'] = sel.xpath('@title').extract()
        #     item['url'] = sel.xpath('@href').extract()
        #     yield item
        for sel in response.css('#content_marcas > div > ul'):
            item = EcpItem()
            item['name'] = sel.xpath('a/text()').extract()
            item['url'] = sel.xpath('a/@href').extract()
            yield item
