# -*- coding: utf-8 -*-
import scrapy
import json

class QuotesScrollSpider(scrapy.Spider):
    name = "quotes_scroll"
    allowed_domains = ["toscrape.com"]
    api_url = 'http://quotes.toscrape.com/api/quotes?page={}'
    start_urls = [api_url.format(1)]

    def parse(self, response):
		data = json.loads(response)
		for quote in data['quotes']:
			yield {
				'author_name': quote['author']['name'],
				'text': quote['text'],
				}
		if data['has_next']:
			next_page = data['page']+1
			yield scrapy.Request(url=self.api_url.format(next_page), callback=self.parse)
