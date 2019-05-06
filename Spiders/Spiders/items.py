# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class SpidersItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class DangDangItem(scrapy.Item):

    title = scrapy.Field()

    detail = scrapy.Field()

    now_price = scrapy.Field()

    pre_price = scrapy.Field()

    discount = scrapy.Field()

    author = scrapy.Field()

    publish = scrapy.Field()

    publish_date = scrapy.Field()

    star = scrapy.Field()

    comment = scrapy.Field()

    image_url = scrapy.Field()

    images = scrapy.Field()

