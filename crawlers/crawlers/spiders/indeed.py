
import scrapy

from ..items import JobItem


class Spider(scrapy.Spider):
    name = 'indeed'
    start_urls = ['https://ar.indeed.com/jobs?q=python+developer&sort=date']

    def parse(self, response):
        cards = response.xpath('//div[@data-tn-component="organicJob"]')
        for card in cards:
            link_element = card.css('h2.jobtitle > a')
            title = link_element.css("::text").extract_first()
            href = 'https://ar.indeed.com{}'.format(
                link_element.xpath('@href').extract_first()
            )
            job_id = card.xpath('@data-jk').extract_first()
            desc = card.css('.summary::text').extract_first().strip()
            company = card.css('.company::text').extract_first()
            data = {
                'job_id': job_id,
                'title': title,
                'link': href,
                'description': desc,
                'company': company,
                'webpage': 'indeed.com'
            }
            JobItem(**data).save()
