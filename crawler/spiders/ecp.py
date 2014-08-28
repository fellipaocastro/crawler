# coding: utf-8

import scrapy


class EcpSpider(scrapy.Spider):
    name = "ecp"
    allowed_domains = ["epocacosmeticos.com.br"]
    start_urls = ["http://www.epocacosmeticos.com.br/perfumes"]

    def parse(self, response):
        filename = "ecp.csv"
        with open(filename, 'wb') as f:
            for sel in response.css('h3 > a[href$="/p"]'):
                name = sel.xpath('text()').extract()
                url = sel.xpath('@href').extract()
                title = sel.xpath('@title').extract()
                f.write("%s - %s - %s\n\n" % (name, url, title))
