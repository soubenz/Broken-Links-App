# -*- coding: utf-8 -*-

import scrapy


class Link(scrapy.Item):
    position = scrapy.Field()
    url = scrapy.Field()
    scanned_website = scrapy.Field()
    webpage = scrapy.Field()
