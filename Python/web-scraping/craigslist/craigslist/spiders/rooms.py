# -*- coding: utf-8 -*-
import scrapy

class Post(scrapy.Item):
    post_id = scrapy.Field()    # .postinginfo:nth-child(1)::text
    price = scrapy.Field()      # .price::text
    sqft = scrapy.Field()       # '.housing::text
    title = scrapy.Field()      # #titletextonly::text
    locality = scrapy.Field()   # .postingtitletext small::text
    lat = scrapy.Field()        # #map::attr(data-latitude)
    lng = scrapy.Field()        # #map::attr(data-longitude)
    imgs = scrapy.Field()       # #thumbs img::attr(src)
    # size = scrapy.Field()       # ' '.join(response.css('.shared-line-bubble:nth-child(1) ::text').extract()[:2])
    att_list = scrapy.Field()   # list = response.css('.attrgroup+ .attrgroup ::text').extract()
                                # list = [s.strip() for s in list]
                                # list = [s for s in listx if s != '']
    post_date = scrapy.Field()  # response.css('.postinginfo:nth-child(2) .timeago::attr(datetime)').extract_first()
    mod_date = scrapy.Field()   # response.css('.postinginfo~ .postinginfo+ .postinginfo .timeago::attr(datetime)').extract_first()
    url = scrapy.Field()

class RoomsSpider(scrapy.Spider):
    name = 'rooms'
    # allowed_domains = ['https://sfbay.craigslist.org']
    start_urls = ['https://sfbay.craigslist.org/search/roo?search_distance=3&postal=94117&availabilityMode=0']

    def parse(self, response):
        # Posting link
        for href in response.css('.hdrlnk::attr(href)').extract():
            request = scrapy.Request(href, callback=self.parse_post)
            yield request

        # Paging
        for href in response.css('.next::attr(href)').extract():
            request = scrapy.Request(response.urljoin(href), callback=self.parse)
            yield request
        
    def parse_post(self, response):
        item = Post()
        item['post_id'] = response.css('.postinginfo:nth-child(1)::text').extract_first()
        item['price'] = response.css('.price::text').extract_first()
        item['title'] = response.css('#titletextonly::text').extract_first()
        item['locality'] =  response.css('.postingtitletext small::text').extract_first().strip()[1:-1]
        item['lat'] = response.css('#map::attr(data-latitude)').extract_first()
        item['lng'] = response.css('#map::attr(data-longitude)').extract_first()
        item['imgs'] = response.css('#thumbs img::attr(src)').extract()  # This is a list
        item['post_date'] = response.css('.postinginfo:nth-child(2) .timeago::attr(datetime)').extract_first()
        item['mod_date'] = response.css('.postinginfo~ .postinginfo+ .postinginfo .timeago::attr(datetime)').extract_first()
        item['url'] = response.url

        # Sqft
        sqft = response.css('.housing::text').extract_first()
        item['sqft'] = sqft[-5:] if sqft else None

        # Attribute list
        atts = response.css('.attrgroup+ .attrgroup ::text').extract()
        atts = [s.strip() for s in atts]
        atts = [s for s in atts if s != '']
        item['att_list'] = atts  # Also a list

        yield item
