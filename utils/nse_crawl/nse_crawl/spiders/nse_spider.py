import scrapy
import os

import sys

# insert at 1, 0 is the script path (or '' in REPL)
from ..items import NseCrawlItem
from dotenv import load_dotenv
from pathlib import Path

dotenv_path = Path('/home/stephenraj/PycharmProjects/The Watcher/.env')
load_dotenv(dotenv_path=dotenv_path)


class NseSpider(scrapy.Spider):
    name = os.getenv('nse_name')
    allowed_domains = os.getenv('nse_domain')
    start_urls = [os.getenv('nse_start_url')]

    def parse(self, response):
        rows = response.xpath("//div[contains(@class,'mw-parser-output')]")
        symbols = rows.xpath(".//table//tbody//tr//td//a[contains(@class,'external text')]/text()").extract()
        company_names = rows.xpath(".//table//tbody//tr//td[last()]/text()").extract()
        company_names = list(map(lambda s: s.strip(), company_names))
        company_names_missed = rows.xpath(".//table//tbody//tr//td[last()]//a/text()").extract()
        j = 0

        for i in range(len(company_names)):
            if company_names[i] == '':
                company_names[i] = company_names_missed[j]
                j += 1
            item = NseCrawlItem()
            item['symbol'] = symbols[i]
            item['company'] = company_names[i]
            yield item
