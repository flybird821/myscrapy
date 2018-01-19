# -*- coding: utf-8 -*-
import scrapy


class Tap150Spider(scrapy.Spider):
    name = 'Tap150'
    #allowed_domains = ['www.taptap.com']
    start_urls=['https://www.taptap.com/top/download?page=2']
    #scrapy.Request(url=start_urls[0],callback=self.geturl)
    #def parse(self):
        #urls = ['https://www.taptap.com/top/download?page=2']
        #for url in urls:
            #yield scrapy.Request(url=url,callback=self.geturl)


    def parse(self, response):
        dict1 = {}
        for i in range(1,31):
            #str1 = 'div:nth-child('+repr(i)+') > div.top-card-middle > a::attr(href)'
            url = response.css('div:nth-child('+repr(i)+') > div.top-card-middle > a::attr(href)').extract_first('url out of range')
            num = response.css('div:nth-child('+repr(i)+') >  span::text').extract_first('num out of range')
            dict1[num] = url
            #i+=1
        yield dict1
