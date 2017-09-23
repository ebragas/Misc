# -*- coding: utf-8 -*-
import scrapy


class SuperchargersSpider(scrapy.Spider):
    name = 'superchargers'
    # allowed_domains = ['https://www.tesla.com/findus/list']
    start_urls = ['http://https://www.tesla.com/findus/list/']

    def parse(self, response):
        pass
