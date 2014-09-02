# coding: utf-8

patterns = {
    "brand_links": "#marcas > div > .menu-departamento > .brandFilter > ul > \
li > a",
    "brand_link_text": "text()",
    "brand_link_href": "@href",
    "brand_name": "div.bread-crumb > ul > li.last > strong > a::text",
    "brand_total_products": "span.resultado-busca-numero > span.value::text",
    "brand_fq": "q=(.+)\&P",
    "product_links": 'h3 > a[href$="/p"]',
    "product_link_href": "@href",
    "product_name": 'div.productName[itemprop="name"]::text',
    "product_title": "title::text"
}
