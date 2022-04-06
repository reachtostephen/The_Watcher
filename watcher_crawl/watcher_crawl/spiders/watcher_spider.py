import scrapy


class WatcherSpiderSpider(scrapy.Spider):
    name = 'watcher_spider'
    allowed_domains = ['economictimes.indiatimes.com']
    start_urls = ['http://economictimes.indiatimes.com/']

    def parse(self, response):
        company_names = ['reliance-industries-ltd', 'hdfc-bank-ltd', 'bajaj-finance-ltd', 'bharti-airtel-ltd',
                         'adani-enterprises-ltd']
        company_codes = [13215, 9195, 11260, 2718, 9074]
        for i in range(len(company_names)):
            yield response.follow(
                f"https://economictimes.indiatimes.com/{company_names[i]}/stocks/companyid-{company_codes[i]}.cms",
                callback=self.parse_company, dont_filter=True,
                meta={'company_name': company_names[i], 'company_code': company_codes[i]})

    def parse_company(self, response):
        company_sector, company_industry = response.css("li::attr(title)").extract()
        tables = response.xpath("//table[contains(@class,'table consolidated')]")
        # self.logger.info(columns)
        yield response.follow(response.url, callback=self.parse_table, meta={
            'tables': tables, 'company_sector': company_sector, 'company_industry': company_industry,
            'company_name': response.meta.get('company_name'), 'company_code': response.meta.get('company_code')},
                              dont_filter=True)

    def parse_table(self, response):
        tables = response.meta.get('tables')
        for columns in tables[0].xpath('.//thead/tr'):
            column_names = columns.xpath('th[re:test(@class,"tb_col_\d$")]/text()').extract()
            column_names = ['fields'] + column_names
        compiled_values = []
        for row in tables[0].xpath('.//tbody/tr'):
            values = row.xpath("td/text()").extract()
            if len(values) == 1:
                values2 = row.xpath("td/span/text()").extract()
                values.extend(values2)
            compiled_values.append(values)
        yield {
            'company_name': response.meta.get('company_name'),
            'company_code': response.meta.get('company_code'),
            'company_sector': response.meta.get('company_sector'),
            'company_industry': response.meta.get('company_industry'),
            'tables': {
                'columns': column_names,
                'values': compiled_values
            }
        }
