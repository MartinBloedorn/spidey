#!/bin/bash
cd spidey_crawler
scrapy crawl gizmodo > gizmodo_crawler_log.txt 2>&1
cd .. 
