# -*- coding:UTF-8 -*-
# 阅
"""
Scrapy signals

These signals are documented in docs/topics/signals.rst. Please don't add new
signals here without documenting them there.
"""

engine_started = object()
engine_stopped = object()
spider_opened = object()
spider_idle = object()
spider_closed = object()
spider_error = object()         # callback里的
request_scheduled = object()    # engine -> schedule
request_dropped = object()      # request <- schedule丢弃
response_received = object()    # engine get
response_downloaded = object()  # downloader -> engine
item_scraped = object()
item_dropped = object()

# for backwards compatibility
stats_spider_opened = spider_opened
stats_spider_closing = spider_closed
stats_spider_closed = spider_closed

item_passed = item_scraped

request_received = request_scheduled
