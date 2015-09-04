# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from spidey_crawler.items import GizmodoEntryItem

import sys, os

# Configures Django models to be acessible from outside the app folder
sys.path.append(os.path.join(os.path.dirname(__file__), '../../'))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "spidey_django.settings")

from scrapy.exceptions import DropItem
from spidey_rest.models import GizmodoEntry


class GizmodoStoringPipeline(object):

    def __init__(self):
        self.post_ids_seen = set()

    def process_item(self, item, spider):

        # Checks if this 'post_id' was already processed
        if item['post_id'] in self.post_ids_seen:
            raise DropItem("Duplicate item found: %s" % item)
        else:
            self.post_ids_seen.add(item['post_id'])

            g_item = GizmodoEntry()
            g_item.author = item['author']
            g_item.post_id = item['post_id']
            g_item.title = item['title']
            g_item.save()

            return item