# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import csv
import os


class LiepinPipeline(object):
    def process_item(self, item, spider):
        headers = ['job', 'salary', 'company', 'age', 'belong', 'experience', 'edu', 'address','address_detail']
        if os.path.isfile('file.csv'):
            with open('file.csv', 'a') as f:
                f_csv = csv.DictWriter(f, headers)
                f_csv.writerows([item])
        else:
            with open('file.csv', 'w') as f:
                f_csv = csv.DictWriter(f, headers)
                f_csv.writeheader()
                f_csv.writerows([item])
            return item
