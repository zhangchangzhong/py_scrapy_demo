# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql

from tutorial import settings


class TutorialPipeline(object):
    total = 0  # 我们自定义的变量，用于统计文章总数

    # open_spider方法在爬虫开始工作之前调用，通常可以初始化环境、打开数据库、打开文件等工作
    def open_spider(self, spider):
        # 这里只显示一行文字作为示例
        print("open spider ...")

    # 这个方法是最基本的方法，每次爬虫parse方法返回一个item的时候，都会调用这个函数，对基本的一个数据单元进行处理
    def process_item(self, item, spider):
        self.total += 1  # 累计文章数
        # 显示基本数据内容，通常可以在这个方法中对数据保存入库、触发分析动作等
        # print("%s %s %s" % (item['date'], item['title'], item['link']))
        # host = settings.MYSQL_HOST
        # user = settings.MYSQL_USER
        # psd = settings.MYSQL_PASSWORD
        # db = settings.MYSQL_DB
        # c = settings.CHARSET
        # port = settings.MYSQL_PORT
        # # 数据库连接
        # con = pymysql.connect(host=host, user=user, passwd=psd, db=db, charset=c, port=port)
        # # 数据库游标
        # cue = con.cursor()
        # print("mysql connect succes")  # 测试语句，这在程序执行时非常有效的理解程序是否执行到这一步
        # # sql="insert into gamerank (rank,g_name,g_type,g_status,g_hot) values(%s,%s,%s,%s,%s)" % (item['rank'],item['game'],item['type'],item['status'],item['hot'])
        # try:
        #     cue.execute("insert into yii (`text`,`time`,`link`,`content`,`readingnum`) values(%s,%s,%s,%s,%s)",
        #                 [item['title'], item['date'], item['link'], item['content'], item['readingnum']])
        #     print("insert success")  # 测试语句
        # except Exception as e:
        #     print('Insert error:', e)
        #     con.rollback()
        # else:
        #     con.commit()
        # con.close()
        return item

    # 所有链接处理完毕，结束爬虫工作时调用，通常可以用于关闭数据库、关闭文件等。
    def close_spider(self, spider):
        # 作为示例，这里只是显示处理结果
        print(u"共", self.total, u"篇文章")
        print("close spider ...")