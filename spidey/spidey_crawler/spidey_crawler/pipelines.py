# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from spidey_crawler.items import GizmodoEntryItem
from scrapy.exceptions import DropItem


class GizmodoStoringPipeline(object):

    def __init__(self):
        self.post_ids_seen = set()

    def process_item(self, item, spider):

        # Checks if this 'post_id' was already processed
        if item['post_id'] in self.post_ids_seen:
            raise DropItem("Duplicate item found: %s" % item)
        else:
            self.post_ids_seen.add(item['post_id'])
            return item
