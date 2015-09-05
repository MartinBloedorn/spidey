#!/bin/bash

# Currently no smart workaround this
SPIDEY_DIR=/home/martin/apps/spidey.git
SCRAPY_BIN=/usr/local/bin/scrapy

# Set automatically
SCWD="$(pwd)"

cd $SPIDEY_DIR/spidey/spidey_crawler
${SCRAPY_BIN} crawl gizmodo > gizmodo_crawler_log.txt 2>&1
cd $SCWD
