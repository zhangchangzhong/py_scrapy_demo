# -*- coding: utf-8 -*-


import scrapy
from scrapy.exceptions import DropItem
from scrapy.pipelines.images import ImagesPipeline


class SaveImagePipeline(ImagesPipeline):

    def get_media_requests(self, item, info):
        print("下载请求开始")
        # 下载图片，如果传过来的是集合需要循环下载
        # meta里面的数据是从spider获取，然后通过meta传递给下面方法：file_path
        yield scrapy.Request(url=item['url'])

    def item_completed(self, results, item, info):
        # 是一个元组，第一个元素是布尔值表示是否成功
        if not results[0][0]:
            raise DropItem('下载失败')
        # 打印日志
        print('下载图片成功')
        return item

    # 重命名，若不重写这函数，图片名为哈希，就是一串乱七八糟的名字
    def file_path(self, request, response=None, info=None):
        print("下载开始")
        return request.url.split('/')[-1]
