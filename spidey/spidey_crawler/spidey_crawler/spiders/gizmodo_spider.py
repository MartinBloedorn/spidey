import re
import scrapy
from scrapy.exceptions import CloseSpider
from spidey_crawler.items import GizmodoEntryItem


class GizmodoSpider(scrapy.Spider):
    name = "gizmodo"
    allowed_domains = ["gizmodo.com"]
    start_urls = ['http://us.gizmodo.com/']
    max_depth = 10

    # Callback method that parses the GET response for each crawled url
    def parse(self, response):
        self.logger.info('A response from %s just arrived!', response.url)

        self.max_depth -= 1
        if self.max_depth <= 0:
            raise CloseSpider('Maximum established depth reached!')

        # Filters the response to correctly fill the item, then yields it to the pipeline
        item = GizmodoEntryItem()
        item['post_id'] = '8t97ts'
        yield item

        # extracting all urls from response, then removing duplicate entries, as seen in:
        # http://stackoverflow.com/questions/7961363/python-removing-duplicates-in-lists
        all_urls = list(set(response.xpath('//a/@href').extract()))
        # preparing regexp: leaves only *.gizmodo.com/* urls
        regex = re.compile('(.*gizmodo\.com\/.*)')
        # Compact application of regexp on all elements of a list
        # as seen in : http://stackoverflow.com/questions/2436607/how-to-use-re-match-objects-in-a-list-comprehension
        valid_urls = [m.group(1) for l in all_urls for m in [regex.search(l)] if m]

        # continuing to scrape the other valid urls
        for url in valid_urls:
            yield scrapy.Request(url, callback=self.parse)

