# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.item import Item,Field


class FirstItem(Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    company_name = Field()
    company_code = Field()
    company_sector = Field()
    company_industry = Field()
    pass

class SecondItem(Item):
    company_code = Field()
    scraped_table = Field()
    columns = Field()
    values = Field()
    pass