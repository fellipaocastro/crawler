# coding: utf-8

import re
import math

import scrapy

from crawler.items import EcpItem


class EcpSpider(scrapy.Spider):
    name = "ecp"
    allowed_domains = ["epocacosmeticos.com.br"]
    start_urls = ["http://www.epocacosmeticos.com.br/marcas"]
    store_total_products = 0

    def parse(self, response):
        self.log("parse: %s" % response.url)

        for sel in response.css("#marcas > div > .menu-departamento > \
.brandFilter > ul > li > a"):
            yield scrapy.Request(
                self.sanitize(sel.xpath("@href").extract()[0]),
                callback=self.parse_brand
            )

    def parse_brand(self, response):
        self.log("parse_brand: %s" % response.url)

        brand_total_products = int(self.sanitize(response.css(
            "span.resultado-busca-numero > span.value::text").extract()[0]))

        self.store_total_products += brand_total_products

        brand_name = self.sanitize(response.css(
            "div.bread-crumb > ul > li.last > strong > a::text").extract()[0])

        self.log("%s has %s products" % (
            brand_name,
            brand_total_products))

        fq = re.search("q=(.+)\&P", self.sanitize(response.css("script")[45]
                                                          .extract())).group(1)

        self.log("fq: %s" % fq)

        self.log("self.store_total_products: %s" % self.store_total_products)
        if brand_total_products <= 20:
            for sel in response.css('h3 > a[href$="/p"]'):
                yield scrapy.Request(
                    self.sanitize(sel.xpath("@href").extract()[0]),
                    callback=self.parse_product
                )
        else:
            brand_total_pages = int(math.ceil(
                float(brand_total_products / 50.0)))

            for i in range(1, brand_total_pages + 1):
                page_url = "http://www.epocacosmeticos.com.br/buscapagina\
?fq=%s&PS=50&sl=3d564047-8ff1-4aa8-bacd-f11730c3fce6&cc=4&sm=0\
&PageNumber=%s" % (fq, i)
                yield scrapy.Request(
                    page_url,
                    callback=self.parse_brand2
                )

    def parse_brand2(self, response):
        self.log("parse_brand2: %s" % response.url)
        for sel in response.css('h3 > a[href$="/p"]'):
            yield scrapy.Request(
                self.sanitize(sel.xpath("@href").extract()[0]),
                callback=self.parse_product
            )

    def parse_product(self, response):
        self.log("parse_product: %s" % response.url)

        item = EcpItem()

        item["name"] = self.sanitize(response.css(
            'div.productName[itemprop="name"]::text').extract()[0])

        item["title"] = self.sanitize(response.css(
            "title::text").extract()[0])

        item["url"] = response.url

        yield item

    def sanitize(self, s):
        return s.strip().replace("\n", "")
