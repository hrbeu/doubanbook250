# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class Doubanbook250Item(scrapy.item.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    name=scrapy.item.Field()
    year=scrapy.item.Field()
    author=scrapy.item.Field()
