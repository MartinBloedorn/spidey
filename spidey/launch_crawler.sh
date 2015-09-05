#!/bin/bash
cd spidey_crawler
/usr/local/bin/scrapy crawl gizmodo > gizmodo_crawler_log.txt 2>&1
cd .. 
