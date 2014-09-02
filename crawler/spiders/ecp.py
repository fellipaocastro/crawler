# coding: utf-8

import re
import math

import scrapy

from crawler.items import EcpItem
from crawler.patterns import patterns


class EcpSpider(scrapy.Spider):
    name = "ecp"

    allowed_domains = ["epocacosmeticos.com.br"]

    site_url = "http://www.%s" % allowed_domains[0]

    start_urls = ["%s/marcas" % site_url]

    products_per_page = 50

    ajax_page_url = "%s/buscapagina?fq=%s&PS=%s&\
sl=3d564047-8ff1-4aa8-bacd-f11730c3fce6&cc=4&sm=0&PageNumber=%s"

    total_brands = 0

    store_total_products = 0

    def parse(self, response):
        self.log("parse: %s" % response.url)

        for sel in response.css(patterns["brand_links"]):

            self.total_brands += 1

            self.log("Brand: %s" % EcpSpider.sanitize(sel.xpath(
                patterns["brand_link_text"]).extract()[0]))

            self.log("self.total_brands: %s" % self.total_brands)

            yield scrapy.Request(
                EcpSpider.sanitize(sel.xpath(patterns["brand_link_href"])
                                      .extract()[0]),
                callback=self.parse_brand_page)

    def parse_brand_page(self, response):
        self.log("parse_brand_page: %s" % response.url)

        brand_name = EcpSpider.sanitize(response.css(
            patterns["brand_name"]).extract()[0])

        brand_total_products = int(EcpSpider.sanitize(response.css(
            patterns["brand_total_products"]).extract()[0]))

        self.store_total_products += brand_total_products

        self.log("self.store_total_products: %s" % self.store_total_products)

        self.log("Brand '%s' has %s products" % (
            brand_name,
            brand_total_products))

        fq = re.search(patterns["brand_fq"], EcpSpider.sanitize(response.css(
            "script").extract()[45])).group(1)

        self.log("fq: %s" % fq)

        brand_total_pages = int(math.ceil(
            float(brand_total_products) / float(self.products_per_page)))

        for i in range(1, brand_total_pages + 1):

            yield scrapy.Request(
                self.ajax_page_url % (
                    self.site_url, fq, self.products_per_page, i),
                callback=self.parse_ajax_brand_page)

    def parse_ajax_brand_page(self, response):
        self.log("parse_ajax_brand_page: %s" % response.url)

        for sel in response.css(patterns["product_links"]):

            yield scrapy.Request(
                EcpSpider.sanitize(sel.xpath(patterns["product_link_href"])
                                      .extract()[0]),
                callback=self.parse_product_page)

    def parse_product_page(self, response):
        self.log("parse_product_page: %s" % response.url)

        item = EcpItem()

        item["name"] = EcpSpider.sanitize(response.css(
            patterns["product_name"]).extract()[0])

        item["title"] = EcpSpider.sanitize(response.css(
            patterns["product_title"]).extract()[0])

        item["url"] = response.url

        yield item

    @staticmethod
    def sanitize(s):
        return s.strip().replace("\n", "")
