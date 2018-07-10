
import scrapy

from ..items import JobItem


class Spider(scrapy.Spider):
    name = 'ziprecruiter'
    start_urls = ['https://www.ziprecruiter.com/candidate/search?search=python+remote&days=10&refine_by_salary=&refine_by_tags=&refine_by_title=&refine_by_org_name=']

    def parse(self, response):
        jobs = response.xpath('//div[@class="job_results"]')
        cards = jobs.xpath("//article")

        for card in cards:
            title = card.xpath('//span[@class="just_job_title"]/text()')
            href = card.xpath('//a[@class="job_link t_job_link"]/@href')
            job_id = link_element.xpath('@data-job-id')
            desc = card.css('.job_snippet > a::text')
            data = {
                'job_id': job_id.extract_first(),
                'title': title.extract_first(),
                'link': href.extract_first(),
                'description': desc.extract_first().strip(),
                'webpage': 'ziprecruiter.com'
            }
            JobItem(**data).save()
