# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import json
import scrapy
from scrapy.exceptions import DropItem
from scrapy.utils.project import get_project_settings
from scrapy.pipelines.images import ImagesPipeline

class SpidersPipeline(object):
    def process_item(self, item, spider):
        return item


class DangDangPipeline(object):

    file = None
    count = 1

    def open_spider(self, spider):

        settings = get_project_settings()
        self.file = open(r"{}dangdang.txt".format(settings.get("DOWNLOAD_DATA_PATH")), "w", encoding="utf-8")

    def process_item(self, item, spider):

        print("start download {} data".format(self.count))
        self.count = self.count + 1

        text = json.dumps(dict(item), ensure_ascii=False) + ",\n"
        self.file.write(text)

        return item

    def close_spider(self, spider):

        self.file.close()
        print("total downloaded record is {}".format(self.count - 1))


class ImagesPipeline(ImagesPipeline):

    def get_media_requests(self, item, info):
        yield scrapy.Request(item['image_url'])

    def item_completed(self, results, item, info):
        image_paths = [x['path'] for ok, x in results if ok]
        if not image_paths:
            raise DropItem("Item contains no images")
        return item


