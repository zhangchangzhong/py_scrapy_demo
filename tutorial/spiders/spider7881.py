# -*- coding: utf-8 -*-
import scrapy

from tutorial.items import ygdyItem


class Spider7881Spider(scrapy.Spider):
    name = 'spider7881'
    allowed_domains = ['www.7881.com']
    start_urls = ['http://www.7881.com/']
    testUrl ='http://pic.7881.com/7881-2016/images/index/dy_logo/dnf.png'

    def parse(self, response):
        # for game in response.xpath('//div[@class="content"]/div[1]//div[@class="hot-game-list"]//div[@class="tab-bottom"]//dl//dd'):
            for image in response.xpath('//img'):
                # gameName=game.css('h2').xpath('a/text()').extract()
                # searchList=game.css('p').xpath('a/@href').extract()
                url = image.xpath('@src').extract_first()
                # print(image)
                print(url)
                item =  ygdyItem()
                item['url']=self.testUrl
                yield item
        # yield  scrapy.Request(self.testUrl)
