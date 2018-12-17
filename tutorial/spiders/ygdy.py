# -*- coding: utf-8 -*-
import scrapy
import time

from tutorial.items import ygdyItem


class YgdySpider(scrapy.Spider):
    name = 'ygdy'
    allowed_domains = ['www.ygdy8.com']
    start_urls = ['http://www.ygdy8.com/']
    baseurl = 'http://www.ygdy8.com'

    # 爬虫入口第一层
    def parse(self, response):
           list =response.xpath('//*[@id="header"]/div/div[3]/div[2]/div[2]/div[1]/div/div[2]/div[2]/ul/table//tr[position()>1]')
           # print(list)
           print(len(list))
           for course in list:
                movieName = course.xpath('.//td[1]/a[2]/text()').extract()[0]
                published = course.xpath(".//td[2]/font/text()").extract()[0]
                movieDetailLink = self.baseurl+course.xpath('.//td[1]/a[2]/@href').extract()[0]
                ygdyItems =ygdyItem()
                ygdyItems['movieName']=movieName
                ygdyItems['published']=published
                ygdyItems['movieDetailLink']=movieDetailLink
           yield scrapy.Request(movieDetailLink,meta={'items':ygdyItems}, callback=self.pare_detail,dont_filter=True)
                # yield ygdyItems


    #爬虫第二层 详情页
    def  pare_detail(self,response):
        ygdyItems=response.meta['items']
        mainDetails=response.xpath('//*[@id="Zoom"]//p[1]')
        images = mainDetails.xpath('./img/@src').extract()
        content =mainDetails.xpath('text()').extract()
        movieDownloadLink =response.xpath('//*[@id="Zoom"]/child::*/child::table/tbody/tr/td/a/text()').extract_first()
        ygdyItems['content']=content
        ygdyItems['imagesUrl']=images
        ygdyItems['movieDownloadLink']=movieDownloadLink
        yield ygdyItems