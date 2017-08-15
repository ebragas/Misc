
import scrapy

class AuthorSpider(scrapy.Spider):
    name = "authors"
    start_urls = ['http://quotes.toscrape.com/']

    def parse(self, response):
        # generate requests for all author pages and parse author
        for href in response.css('.author + a::attr(href)'):
            yield response.follow(href, callback=self.parse_author)

        # follow paginatioin links and parse
        for href in response.css('li.next a::attr(href)'):
            yield response.follow(href, callback=self.parse)

    def parse_author(self, response):
        # method for extracting clean text
        def extract_with_css(query):
            return response.css(query).extract_first().strip()

        yield {
            "name": extract_with_css('h3.author-title::text'),
            "birthdate": extract_with_css('.author-born-date::text'),
            "bio": extract_with_css('.author-description::text')
        }