# Parses quote, author, and tag data from quotes pages and generates request for  next page

import scrapy

class QuotesSpider(scrapy.Spider):
    name = "quotes"
    start_urls = [
        'http://quotes.toscrape.com/page/1/',
    ]

    def parse(self, response):
        for quote in response.css('div.quote'):
            yield {
                'text': quote.css('span.text::text').extract_first(),
                'author': quote.css('small.author::text').extract_first(),
                'tags': quote.css('div.tags a.tag::text').extract()
            }

        next_page = response.css('li.next a::attr(href)').extract_first()
        if next_page is not None:
            # next_page = response.urljoin(next_page)  # Create full URL from relative and root
            # yield scrapy.Request(next_page, callback=self.parse)
            
            yield response.follow(next_page, callback=self.parse)  # Supports relative URLs directly
                                                                   # Also can accept selector instead of url string


