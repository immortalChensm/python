# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

#下载页面---解析提取数据--封装数据---处理/过滤数据
class RateingConverterPipeline(object):
    rating_map = {
        "One":1,
        "Two":2,
        "Three":3,
        "Four":4,
        "Five":5
    }
    def process_item(self, item, spider):
        item['rating'] = self.rating_map[item['rating']]

        return item

class PriceConverterPipeline(object):
    exchange_rate = 8.53
    def process_item(self, item, spider):
        rmb = float(item['price'][1:]) * self.exchange_rate
        item['price'] = "%.2f" % rmb
        return item

from scrapy.exceptions import DropItem
class RatingFilterPipeline(object):

    def __init__(self,filter_level):
        self.filter_level = filter_level
    #读取配置文件的配置参数
    @classmethod
    def from_crawler(cls,crawler):
        filter_level = crawler.settings.get('RATING_FILTER_ITEM',0)
        return cls(filter_level)
    def process_item(self, item, spider):

        if item['rating'] < self.filter_level:
            raise DropItem("drop book %s"%item['name'])
        return item
