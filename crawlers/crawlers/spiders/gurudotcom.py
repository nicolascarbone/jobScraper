
import scrapy

# from jobs.models import GuruJob
from ..items import JobItem


class Spider(scrapy.Spider):
    name = 'gurudotcom'
    start_urls = ['https://www.guru.com/d/freelancers/q/python-remote/']

    def parse(self, response):
        cards = response.css('#serviceList > li')
        for card in cards:
            link_element = card.css('.servTitle > h2 > a')
            title = link_element.css("::text").extract_first()
            href = 'https://guru.com{}'.format(
                link_element.xpath('@href').extract_first()
            )
            job_id = card.xpath('@gid').extract_first()
            desc = card.css('.serviceMeta > p.desc::text').extract_first()
            data = {
                'job_id': job_id,
                'title': title,
                'link': href,
                'description': desc.strip(),
                'webpage': 'guru.com'
            }
            JobItem(**data).save()
