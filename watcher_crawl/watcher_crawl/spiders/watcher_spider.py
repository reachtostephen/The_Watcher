import os
import scrapy

from dotenv import load_dotenv
from pathlib import Path

dotenv_path = Path('/home/stephenraj/PycharmProjects/The Watcher/.env')
load_dotenv(dotenv_path=dotenv_path)


class WatcherSpiderSpider(scrapy.Spider):
    name = os.getenv('spider_name')
    allowed_domains = os.getenv('domain')
    start_urls = [os.getenv('start_url')]

    def parse(self, response):
        company_names = [i.strip() for i in os.getenv('company_names').split(',')]
        company_codes = [int(i) for i in os.getenv('company_codes').split(',')]
        for i in range(len(company_names)):
            yield response.follow(
                f"{os.getenv('start_url')}/{company_names[i]}/stocks/companyid-{company_codes[i]}.cms",
                callback=self.parse_company, dont_filter=True,
                meta={'company_name': company_names[i], 'company_code': company_codes[i]})

    def parse_company(self, response):
        company_sector, company_industry = response.css("li::attr(title)").extract()
        tables = response.xpath("//table[contains(@class,'table consolidated')]")
        yield response.follow(response.url, callback=self.parse_table, meta={
            'tables': tables, 'company_sector': company_sector, 'company_industry': company_industry,
            'company_name': response.meta.get('company_name'), 'company_code': response.meta.get('company_code')},
                              dont_filter=True)

    def parse_table(self, response):
        tables = response.meta.get('tables')
        scraped_tables = ['income_quaterly', 'income_annual', 'balance_sheet', 'cash_flow', 'ratios']
        for i in range(len(tables)):
            for columns in tables[i].xpath('.//thead/tr'):
                column_names = columns.xpath('th[re:test(@class,"tb_col_\d$")]/text()').extract()
                column_names = [i.replace("\n", "").strip() for i in column_names]
                column_names = ['fields'] + column_names
            compiled_values = []
            for row in tables[i].xpath('.//tbody/tr'):
                values = row.xpath("td/text()").extract()
                if len(values) == 1:
                    values2 = row.xpath("td/span/text()").extract()
                    values.extend(values2)
                compiled_values.append(values)

            item = {
                'company_code': response.meta.get('company_code'),
                'scraped_table': scraped_tables[i],
                'columns': column_names,
                'values': compiled_values,
                'company_name': response.meta.get('company_name'),
                'company_sector': response.meta.get('company_sector'),
                'company_industry': response.meta.get('company_industry')
            }
            yield item
