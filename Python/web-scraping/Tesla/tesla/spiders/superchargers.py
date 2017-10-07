# -*- coding: utf-8 -*-
import scrapy

class Country(scrapy.Item):
    country = scrapy.Field()

class State(Country):
    state = scrapy.Field()

class Profile(State):
    name = scrapy.Field()               # #find-us-list-container h1
    common_address = scrapy.Field()     # .common-name
    street_address = scrapy.Field()     # .street-address
    locality = scrapy.Field()           # .locality
    img_src = scrapy.Field()            # img::attr(src)
    availability = scrapy.Field()       # .coming-soon
    chargers = scrapy.Field()

class SuperchargersSpider(scrapy.Spider):
    name = 'superchargers'
    # allowed_domains = ['https://www.tesla.com/findus/list']
    start_urls = ['https://www.tesla.com/findus/list']

    def parse(self, response):
        """Find Country list pages; pass country name through Supercharger item"""

        for i in range(len(response.css('.row:nth-child(5) a').extract())):
            item = Country()
            item['country'] = response.css('.row:nth-child(5) span::text')[i].extract().strip()

            href = response.css('.row:nth-child(5) a::attr(href)')[i].extract()

            request = scrapy.Request(response.urljoin(href), callback=self.parse_country)
            request.meta['item'] = item
            yield request

    def parse_country(self, response):
        """Parse state and charger listings to retrieve profile url"""

        # TODO: Add state name to meta item
        # country_item = response.meta['item']
        item = State()
        item['country'] = response.meta['item']['country']

        # Requests for profiles
        for href in response.css('.url::attr(href)').extract():
            request = scrapy.Request(response.urljoin(href), callback=self.parse_profile)
            request.meta['item'] = item

            # yield {'country': item['country'], 'href': href}
            yield request

    def parse_profile(self, response):
        """Parse profiles to create supercharger item and yield dictionary"""

        item = Profile()
        item['country'] = response.meta['item']['country']

        # Profile data
        item['name'] = response.css('#find-us-list-container h1::text').extract_first()
        item['common_address'] = response.css('.common-name::text').extract_first()
        item['street_address'] = response.css('.street-address::text').extract_first()
        item['locality'] = response.css('.locality::text').extract_first()
        item['img_src'] = response.css('img::attr(src)').extract_first()
        item['availability'] = response.css('.coming-soon::text').extract_first()

        # Find supercharger stats
        for p in range(len(response.css('p'))):
            value = response.css('p::text')[p].extract().strip()
            if "superchargers" in value:
                item['chargers'] = value

        yield item
