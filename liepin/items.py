# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class LiepinItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    job = scrapy.Field()
    edu = scrapy.Field()
    company = scrapy.Field()
    salary = scrapy.Field()
    belong = scrapy.Field()
    experience = scrapy.Field()
    address = scrapy.Field()
    address_detail = scrapy.Field()
    age = scrapy.Field()

