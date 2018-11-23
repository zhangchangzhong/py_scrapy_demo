# -*- coding: utf-8 -*  -
import re
import scrapy

from tutorial.items import FormoonItem


class TpdemoSpider(scrapy.Spider):
    name = 'tpDemo'
    allowed_domains = ['www.yiichina.com']
    start_urls = ['http://www.yiichina.com/news/']
    baseurl = 'http://www.yiichina.com'

    def parse(self, response):
        for course in response.xpath('//ul[@class="news-list"]//li[@class="mb-3"]'):
            time = course.css('.time').xpath('text()').extract_first()
            title = course.css('h2 a').xpath('text()').extract_first()
            link = course.css('h2 a').xpath('@href').extract_first()
            # 区别从这里开始，我们删除了直接显示数据，初始化一个空白的item,将数据填充进去
            item = FormoonItem()
            item['date'] = time
            item['link'] = link
            item['title'] = title
            # yield item  # 将数据返回
            yield scrapy.Request(self.baseurl +link , meta={'item': item}, callback=self.pare_detail,dont_filter=True)
        # for btn in response.css(".page-item.active").xpath('a'):
        #     href = btn.xpath('@href').extract_first()
        #     pageNum = re.findall('(\d+)', href)
        #     pageString = re.findall('(\D+)', href)
        #     # href = btn.xpath('@href').extract()[0]
        #     # name = btn.xpath('button/text()').extract()[0]
        #     # if name == u"下一页":
        #     nextNum=int(pageNum[0])+int(1)
        #     url=self.baseurl + str(pageString[0])+str(nextNum)
        #     yield scrapy.Request(url, callback=self.parse)



    def pare_detail(self,response):
        item=response.meta['item']
        item['content']=response.xpath('//div[@class="markdown"]/p[1]/text()').extract()[1]
        item['readingnum']=response.xpath('//div[@class="action"]/span[2]/text()').extract_first()
        print(item)
        yield item
