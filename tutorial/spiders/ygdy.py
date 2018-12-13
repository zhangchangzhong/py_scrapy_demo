# -*- coding: utf-8 -*-
import scrapy

from tutorial.items import ygdyItem


class YgdySpider(scrapy.Spider):
    name = 'ygdy'
    allowed_domains = ['www.ygdy8.com']
    start_urls = ['http://www.ygdy8.com/']
    baseurl = 'http://www.ygdy8.com'

    # 爬虫入口第一层
    def parse(self, response):
        # for course in response.xpath('//div[@id="header"]/div[1]//div[@class="bd3"]//div[@class="bd3l"]/div[1]'):
        #     listName = course.css('p').xpath('text()').extract_first()
            # contentList = course.xpath('//div[@class="co_content2"]//ul/a')
            # print(listName)
            # print(contentList)
            # print(course)
            # for content in contentList:
                ygdyItems =ygdyItem()
                # movieLink = self.baseurl+content.xpath('@href').extract_first()
                movieLink = self.baseurl+'/html/gndy/dyzz/20181208/57909.html'
            #     movieTitle = content.xpath('text()').extract_first()
                print(movieLink)
            #     print(movieTitle)
                yield scrapy.Request(movieLink,meta={'items':ygdyItems}, callback=self.pare_detail,dont_filter=True)


    #爬虫第二层 详情页
    def  pare_detail(self,response):
        items=response.meta['items']
        mainDetails=response.xpath('//div[@id="header"]/div[1]//div[@class="bd3"]//div[@class="bd3r"]/div[2]//div[@class="co_content8"]//ul')
        published = mainDetails.xpath('text()').extract_first()
        print(mainDetails)
        print(published)