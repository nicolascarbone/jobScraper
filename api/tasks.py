import importlib

from celery import task
from scrapy.crawler import CrawlerProcess


def run_spider(spider):
    process = CrawlerProcess()
    process.crawl(spider)
    process.start()


@task
def scrawl(spider_name):
    spider_module = importlib.import_module(
        'crawlers.crawlers.spiders.{}'.format(spider_name)
    )
    spider = getattr(spider_module, 'Spider')
    run_spider(spider)


@task
def scrawl_all():
    available_spiders = ['gurudotcom', 'ziprecruiter', 'indeed']
    for spider in available_spiders:
        scrawl.delay(spider)
