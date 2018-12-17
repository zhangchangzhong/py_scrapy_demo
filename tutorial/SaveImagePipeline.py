# -*- coding: utf-8 -*-
import os
import scrapy
import shutil
from scrapy.exceptions import DropItem
from scrapy.pipelines.images import ImagesPipeline

from tutorial import settings


class SaveImagePipeline(ImagesPipeline):

    def get_media_requests(self, item, info):
        print("下载请求开始")
        # 下载图片，如果传过来的是集合需要循环下载
        # meta里面的数据是从spider获取，然后通过meta传递给下面方法：file_path
        imagesUrl =item['imagesUrl']
        for image in imagesUrl:
            yield scrapy.Request(url=image)

    def item_completed(self, results, item, info):
        image_paths = {x['url'].split('/')[-1]: x['path'] for ok, x in results if ok}
        print(results)
        if not image_paths:
            # 下载失败忽略该 Item 的后续处理
            raise DropItem("Item contains no files")
        else:
            # 将图片转移至自定义文件名的子目录中
            for (dest, src) in image_paths.items():
                dir = settings.IMAGES_STORE
                newdir = dir +'/' + item['published'] + '/'
                # 判断文件是否存在，不存在则创建
                if not os.path.exists(newdir):
                    os.makedirs(newdir)
                # 移动文件到指定目录
                shutil.move(dir +"/"+ src, newdir +src)
        # 将保存路径保存于 item 中（image_paths 需要在 items.py 中定义）
        item['image_paths'] = image_paths
        return item

    # 重命名，若不重写这函数，图片名为哈希，就是一串乱七八糟的名字
    def file_path(self, request, response=None, info=None):
        file_name = request.url.split('/')[-1]
        return file_name
