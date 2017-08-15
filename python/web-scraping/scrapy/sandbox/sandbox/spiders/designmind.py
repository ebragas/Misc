# -*- coding: utf-8 -*-
import scrapy


class DesignmindSpider(scrapy.Spider):
    name = 'designmind'
    allowed_domains = ['www.designmind.com']
    start_urls = ['http://www.designmind.com/']

    def parse(self, response):
        pass
