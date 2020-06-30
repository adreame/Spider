# -*- coding: utf-8 -*-
import scrapy
import re


class RenrenSpider(scrapy.Spider):
    name = 'renren'
    allowed_domains = ['renren.com']
    start_urls = ['http://www.renren.com/327550029/profile']

    def start_requests(self):
        cookies = ""
        cookies = {i.split("=")[0]:i.split("=")[1] for i in cookies.split("; ")}
        # headers = {"Cookie":cookies}
        yield scrapy.Request(
            self.start_urls[0],
            callback=self.parse,
            cookies=cookies
            # headers = headers
        )

    def parse(self, response):
        print(re.findall("毛兆军",response.body.decode()))
        yield scrapy.Request(
            "http://www.renren.com/327550029/profile?v=info_timeline",
            callback=self.parse_detial
        )

    def parse_detial(self,response):
        print(re.findall("毛兆军",response.body.decode()))
