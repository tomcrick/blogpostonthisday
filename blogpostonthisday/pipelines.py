# -*- coding: utf-8 -*-
from datetime import date

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


class BlogpostonthisdayPipeline(object):
    def process_item(self, item, spider):
        if item['date'].day == date.today().day:
            print(item['title'])
            print(item['url'])
            print(item['date'])
