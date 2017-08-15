# -*- coding: utf-8 -*-
import scrapy


class CcdSpider(scrapy.Spider):
    name = 'ccd'
    # allowed_domains = ['https://www.concretedisciples.com/']
    start_urls = ['https://www.concretedisciples.com/']

    def parse(self, response):
        for url in response.css('.jrContentTitle a::attr(href)').extract():
            yield response.follow(url, callback=self.parse_profile)

        next_page = response.css('.jrPaginationBottom .jr-pagenav-next::attr(href)').extract_first()
        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)

    def parse_profile(self, response):
        desc = response.css('.jrListingFulltext p::text').extract()
        desc = ' '.join(desc)

        yield {
            # General
            "name": response.css('.jrSkateparkname .jrFieldValue::text').extract_first(),
            "has-bmx": response.css('.jrBmx .jrFieldValue::text').extract_first(),
            "open-closed": response.css('.jrRip .jrFieldValue::text').extract_first(),
            "free-or-pay": response.css('.jrFreepayx .jrFieldValue::text').extract_first(),
            "inside-or-outside": response.css('.jrIndoorsx .jrFieldValue::text').extract_first(),
            "has-lights": response.css('.jrLightsx .jrFieldValue::text').extract_first(),
            "pads-required": response.css('.jrPadsx .jrFieldValue::text').extract_first(),
            "riding-surface": response.css('.jrSurfacex .jrFieldValue::text').extract_first(),
            "has-lights": response.css('.jrLightsx .jrFieldValue::text').extract_first(),
            "has-restrooms": response.css('.jrRestroomsx .jrFieldValue::text').extract_first(),
            "has-pro-shop": response.css('.jrProshopx .jrFieldValue::text').extract_first(),
            # Construction
            "designer": response.css('.jrDesignerx a::text').extract_first(),
            "builder": response.css('.jrBuilderx a::text').extract_first(),
            # Address
            "address": response.css('.jrAddress .jrFieldValue::text').extract_first(),
            "zipcode": response.css('.jrZip .jrFieldValue::text').extract_first(),
            "city": response.css('.jrCity .jrFieldValue::text').extract_first(),
            "desc": desc,
            "editor-rating": response.css('.jrOverallEditor .jrRatingValue::text').extract_first(),
            "user-rating": response.css('.jrOverallUser .jrRatingValue::text').extract_first(),
            "size": response.css('.jrSize .jrFieldValue::text').extract_first(),
            "management": response.css('.jrManagement .jrFieldValue::text').extract_first(),
            "views": response.css('.jrListingStatus > span:nth-child(1)::text').extract_first(),
            "favorites": response.css('.jr-favorite-26321::text').extract_first(),
            # Contacts
            "phone": response.css('.jrPhone .jrFieldValue::text').extract_first(),
            "website": response.css('.jrWebsite a::text').extract_first(),
        }
