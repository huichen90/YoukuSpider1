# -*- coding: utf-8 -*-
import scrapy


class YoukuSpider(scrapy.Spider):
    name = 'youku'
    allowed_domains = ['www.soku.com']
    start_urls = ['http://www.soku.com/']

    def parse(self, response):
        pass
