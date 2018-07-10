# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

# import scrapy


# class CrawlersItem(scrapy.Item):
#     # define the fields for your item here like:
#     # name = scrapy.Field()
#     pass


from scrapy_djangoitem import DjangoItem

from jobs.models import Job


class JobItem(DjangoItem):
    django_model = Job
