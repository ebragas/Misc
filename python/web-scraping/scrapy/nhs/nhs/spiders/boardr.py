import scrapy

class skaters(scrapy.Spider):
    name = "boardr"
    start_urls = [
        "https://theboardr.com/skateboarders_list"
    ]

    def parse(self, response):
        for href in response.css('div.col-2 a::attr(href)').extract():
            yield response.follow(href, callback=self.parse_profiles)

    # def parse_profiles(self, response):
    def parse_profiles(self, response):
        for href in response.css('#cphMain_pnlList a::attr(href)').extract():
            yield response.follow(href, callback=self.parse_skater)

    def parse_skater(self, response):
        # yield {
        return {
            # General
            "name": response.xpath('//h1/text()').extract_first(),
            "bio": response.xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "col-12", " " )) and contains(concat( " ", @class, " " ), concat( " ", "col-sm-6", " " ))]//p/text()').extract_first().strip(),
            "sponsers": response.css('.row.well .col-sm-6+ .col-sm-6::text')[4].extract().strip(),
            "insta-followers": response.xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "col-6", " " )) and contains(concat( " ", @class, " " ), concat( " ", "text-center", " " )) and (((count(preceding-sibling::*) + 1) = 2) and parent::*)]//a/text()').extract_first(),
            "insta-rank": response.css('.col-6.text-center:nth-child(3) a::text').extract_first(),
            "yt-views": response.css('.text-center~ .col-12+ .text-center a::text').extract_first(),
            "yt-rank": response.css('.col-6.text-center:nth-child(6) a::text').extract_first(),
            "funded": response.css('.text-center:nth-child(1) h3::text').extract_first(),
            "paid": response.css('.col-4:nth-child(2) h3::text').extract_first(),
            "backers": response.css('.col-4.text-center a::text').extract_first(),
            # Global Rankings
            # "rank-ov": response.css('#profileRanking a::text').extract_first(),
            # "rank-cy": response.css('#profileRanking .col-3:nth-child(7)::text').extract_first(),
            # "rank-ly": response.css('#profileRanking .col-3:nth-child(8)::text').extract_first(),
            # "pts-ov": response.css('.col-3:nth-child(10)::text').extract_first(),
            # "pts-cy": response.css('.text-center:nth-child(11)::text').extract_first(),
            # "pts-ly": response.css('.col-3:nth-child(12)::text').extract_first(),
            # "earnings-ov": response.css('.col-3:nth-child(14)::text').extract_first(),
            # "earnings-cy": response.css('.col-3:nth-child(15)::text').extract_first(),
            # "earnings-ly": response.css('.text-center:nth-child(16)::text').extract_first(),
            # By Discipline
            # "street-ov-rank": response.css('.col-2:nth-child(7)::text').extract_first(),
            # "street-ov-pts": response.css('.col-2:nth-child(8)::text').extract_first(),
            # "street-cy-rank": response.css('.col-2:nth-child(9)::text').extract_first(),
            # "street-cy-pts": response.css('.col-2:nth-child(10)::text').extract_first(),
            # "park-ov-rank": response.css('.col-2:nth-child(12)::text').extract_first(),
            # "park-ov-pts": response.css('.col-2:nth-child(13)::text').extract_first(),
            # "park-cy-rank": response.css('.col-2:nth-child(14)::text').extract_first(),
            # "park-cy-pts": response.css('.col-2:nth-child(15)::text').extract_first(),
            # "vertbowl-ov-rank": response.css('.text-center:nth-child(17)::text').extract_first(),
            # "vertbowl-ov-pts": response.css('.text-center:nth-child(18)::text').extract_first(),
            # "vertbowl-cy-rank": response.css('.text-center:nth-child(19)::text').extract_first(),
            # "vertbowl-cy-pts": response.css('.text-center:nth-child(20)::text').extract_first(),
            # "mega-ov-rank": response.css('.text-center:nth-child(22)::text').extract_first(),
            # "mega-ov-pts": response.css('.text-center:nth-child(23)::text').extract_first(),
            # "mega-cy-rank": response.css('.text-center:nth-child(24)::text').extract_first(),
            # "mega-cy-pts": response.css('.text-center:nth-child(25)::text').extract_first()
        }
