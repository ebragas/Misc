# -*- coding: utf-8 -*-
import scrapy


class SpotSpider(scrapy.Spider):
    name = 'spot'
    # allowed_domains = ['http://skateparkoftampa.com']
    start_urls = ['http://http://skateparkoftampa.com/']

    def parse(self, response):
        for url in response.css('.BlogPost div .SizeSelectionGridItemSmall a::attr(href)').extract():
            yield response.follow(url, callback=self.parse_list)

    def parse_list(self, response):
        for url in response.css('h1+ .BlogPost a::attr(href)').extract():
            yield response.follow(url, callback=self.parse_profile)

    def parse_profile(self, response):
        yield {
            "name": response.css('.PostMediaStripSub+ h1::text').extract_first(),
            "sponsors": response.css('p::text')[0].extract().strip(),
            "bio": response.css('p::text')[-1].extract().strip()
        }
