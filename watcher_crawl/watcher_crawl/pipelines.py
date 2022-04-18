import pymongo
import pandas as pd
from scrapy.utils.project import get_project_settings


class WatcherCrawlPipeline:
    def __init__(self):
        settings = get_project_settings()
        connection = pymongo.MongoClient(
            settings.get('MONGODB_SERVER'),
            settings.get('MONGODB_PORT')
        )
        self.db = connection[settings.get('MONGODB_DB')]
        self.collection = self.db[settings.get('MONGODB_COLLECTION')]

    def process_item(self, item, spider):
        dict1 = {
            'company_code': item['company_code'],
            'company_name': item['company_name'],
            'company_industry': item['company_industry'],
            'company_sector': item['company_sector']
        }
        is_existing = self.collection.find_one(dict1)
        if not is_existing:
            self.collection.insert_one(dict1)

        coll = self.db[item['scraped_table']]
        coll_names = item['columns']
        df = pd.DataFrame(item['values'], columns=coll_names)
        df.set_index('fields', inplace=True)
        df2 = df.T
        df2.reset_index(inplace=True)
        df2['company_code'] = item['company_code']
        coll.insert_many(df2.to_dict('records'))
        for i in coll.find({"company_code": item['company_code']}):
            self.collection.update_one({'company_code': item['company_code']}, {'$push': {'ref': i['_id']}})
