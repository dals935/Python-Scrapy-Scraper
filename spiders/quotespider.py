import scrapy

class QuoteSpider(scrapy.Spider):
    name = 'quote'
    start_urls = ['https://quotes.toscrape.com/tag/inspirational/']
    
    def parse(self, response):
        for quotes in response.css('div.quote'):
            yield {
                'quote': quotes.css('span.text::text').get(),
                'author': quotes.css('small.author::text').get()
            }
        next_page = response.css('li.next a::attr(href)').get()
        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)