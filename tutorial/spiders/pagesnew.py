# -*- coding: utf-8 -*-
import scrapy

from tutorial.items import FormoonItem


class PagesnewSpider(scrapy.Spider):
    name = 'pagesnew'
    allowed_domains = ['formoon.github.io']
    start_urls = ['https://formoon.github.io/']

    baseurl = 'https://formoon.github.io'

    def parse(self, response):
        for course in response.xpath('//ul/li'):
            href = self.baseurl + course.xpath('a/@href').extract()[0]
            title = course.css('.card-title').xpath('text()').extract()[0]
            date = course.css('.card-type.is-notShownIfHover').xpath('text()').extract()[0]
            # 区别从这里开始，我们删除了直接显示数据，初始化一个空白的item,将数据填充进去
            item = FormoonItem()
            item['date'] = date
            item['link'] = href
            item['title'] = title
            yield item  # 将数据返回
        for btn in response.css('.container--call-to-action').xpath('a'):
            href = btn.xpath('@href').extract()[0]
            name = btn.xpath('button/text()').extract()[0]
            if name == u"下一页":
                yield scrapy.Request(self.baseurl + href, callback=self.parse)