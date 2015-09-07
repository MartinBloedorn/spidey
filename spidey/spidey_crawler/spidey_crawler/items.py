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
    post_date = scrapy.Field()
    description = scrapy.Field()
    keywords = scrapy.Field()
    text = scrapy.Field()
    url = scrapy.Field()

    def __repr__(self):
        """only print out title after exiting the Pipeline"""
        return repr({"Title": self['title']})
