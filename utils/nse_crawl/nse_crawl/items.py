
import scrapy
from scrapy.item import Item, Field


class NseCrawlItem(scrapy.Item):
    symbol = Field()
    company = Field()
