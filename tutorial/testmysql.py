# -*- coding: utf-8 -*-
import pymysql

import tutorial
from tutorial import settings


def process_item():
    # 显示基本数据内容，通常可以在这个方法中对数据保存入库、触发分析动作等
    # print("%s %s %s" % (item['date'], item['title'], item['link']))
    settings = tutorial.settings;
    host = settings.MYSQL_HOST
    user = settings.MYSQL_USER
    psd = settings.MYSQL_PASSWORD
    db = settings.MYSQL_DB
    c = settings.CHARSET
    port = settings.MYSQL_PORT
    # 数据库连接
    con = pymysql.connect(host=host, user=user, passwd=psd, db=db, charset=c, port=port)
    # 数据库游标
    cue = con.cursor()
    print("mysql connect succes")  # 测试语句，这在程序执行时非常有效的理解程序是否执行到这一步
    # sql="insert into gamerank (rank,g_name,g_type,g_status,g_hot) values(%s,%s,%s,%s,%s)" % (item['rank'],item['game'],item['type'],item['status'],item['hot'])
    try:
        cue.execute("insert into yii (`text`,`time`,`content`) values('发布于 2018-09-23 ','Debug 扩展 2.0.14 版本发布了','/news/183')")
        print("insert success")  # 测试语句
    except Exception as e:
        print('Insert error:', e)
        con.rollback()
    else:
        con.commit()
    con.close()

if __name__ =="__main__":
    process_item()