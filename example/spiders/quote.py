import scrapy


class QuotesSpider(scrapy.Spider):
    name = "quotes"

    def start_requests(self):
        urls = [
            'https://www.bild.de',
            'https://www.chip.de',
            'https://www.zdf.de',
            'https://www.postbank.de',
            'https://www.focus.de',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        page = response.url.split("www.")[1]
        page = page.split('.')[0]
        filename = '%s.html' % page
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log('Saved file %s' % filename)
