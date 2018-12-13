# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class FormoonItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # 以上是模板中已经有的内容，下面是我们自己增加的3个字段
    title = scrapy.Field()
    link = scrapy.Field()
    date = scrapy.Field()
    content = scrapy.Field()
    readingnum = scrapy.Field()


class ygdyItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # 以上是模板中已经有的内容，下面是我们自己增加的3个字段
    title = scrapy.Field()
    link = scrapy.Field()
    date = scrapy.Field()
    content = scrapy.Field()
    readingnum = scrapy.Field()
    url = scrapy.Field()