import scrapy
from scrapy.exceptions import CloseSpider
from spidey_crawler.items import GizmodoEntryItem


class GizmodoSpider(scrapy.Spider):
    name = "gizmodo"
    allowed_domains = ["gizmodo.com"]
    start_urls = ['http://us.gizmodo.com/']

    # Maximum number of urls
    max_expansions = 10

    # Regex for date field and valid URL (to crawl)
    re_id = 'date:\s*new\s*Date\(\'(\w+)\'\)'
    re_url = '(.*gizmodo\.com\/.*)'
    re_date = '"datePublished":"([\w\-:]*)"'

    # Callback method that parses the GET response for each crawled url
    def parse(self, response):
        self.logger.info('A response from %s just arrived!', response.url)

        self.max_expansions -= 1
        if self.max_expansions <= 0:
            raise CloseSpider('Reached maximum of URL crawls!')

        # Verify if page is of type 'article'
        type = response.xpath('//meta[@property="og:type"]/@content').extract()
        if type.__len__() > 0 and type[0] == 'article':

            # Filters the response to correctly fill the item, then yields it to the pipeline
            item = GizmodoEntryItem()
            item['author'] = response.xpath('//meta[@name="author"]/@content').extract()[0]
            item['title'] = response.xpath('//meta[@property="og:title"]/@content').extract()[0]
            item['keywords'] = response.xpath('//meta[@name="keywords"]/@content').extract()[0]
            item['description'] = response.xpath('//meta[@name="description"]/@content').extract()[0]
            # Uses the JavaScript date (milliseconds since the epoch) as post_id
            item['post_id'] = response.xpath('//script/text()').re(self.re_id)[0]
            item['post_date'] = response.xpath('//script/text()').re(self.re_date)[0]
            # Join all elements of the query in a single block of text, breaking lines at each paragraph
            item['text'] = '\n'.join(response.xpath('//p[@data-textannotation-id]').extract())
            item['url'] = response.url
            yield item

        # from all urls on the page, follow only absloute ones in the gizmodo domain name
        valid_urls = response.xpath('//a/@href').re(self.re_url)

        # continuing to scrape the other valid urls
        for url in valid_urls:
            yield scrapy.Request(url, callback=self.parse)

