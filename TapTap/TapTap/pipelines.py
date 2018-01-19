# -*- coding: utf-8 -*-
import pymongo
from pymongo import MongoClient
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

class TaptapPipeline(object):
    def process_item(self, item, spider):
    #     try:
    #         line = str(dict(item))+"\n"
    #         self.f.write(line)
    #     except:
    #         pass
        self.coll.insert(dict(item))
        return item
    def close_spider(self,spider):
        #self.f.close()
        self.client.close()
    def open_spider(self,spider):
        #self.f = open('result.txt','w')
        self.client = MongoClient()
        self.db = self.client.pymongo_taptap
        self.coll = self.db.paiming
