# -*- coding: utf-8 -*-
import scrapy


class FolloLinksSpider(scrapy.Spider):
    name = "follow_link"
    allowed_domains = ["toscrape.com"]
    start_urls = (
        'http://quotes.toscrape.com/',
    )

    def parse(self, response):
        for quote in response.css('div.quote'):
            item = {
                'author_name': quote.css('small.author::text').extract_first(),
                'text': quote.css('span.text::text').extract_first()
            }
            yield item
            next_page_url = response.css('li.next > a::attr(href)').extract_first()
            if next_page_url:
                next_page_url  = response.urljoin(next_page_url)
                yield scrapy.Request(url=next_page_url, callback=self.parse)