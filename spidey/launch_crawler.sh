#!/bin/bash

# Currently no smart workaround this
SPIDEY_DIR=/home/martin/apps/spidey.git
SCRAPY_BIN=/usr/local/bin/scrapy
SCRAPY_LOG=/home/martin/apps/gizmodo_crawler_log.txt

# Set automatically
SCWD="$(pwd)"

cd $SPIDEY_DIR/spidey/spidey_crawler
${SCRAPY_BIN} crawl gizmodo -s LOG_FILE=$SCRAPY_LOG
cd $SCWD
