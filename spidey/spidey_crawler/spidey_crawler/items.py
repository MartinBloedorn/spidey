# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class GizmodoEntryItem(scrapy.Item):
    author = scrapy.Field()
    title = scrapy.Field()
    post_id = scrapy.Field()
    text = scrapy.Field()
