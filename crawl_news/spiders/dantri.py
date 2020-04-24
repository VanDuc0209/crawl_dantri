# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Request
import datetime


class DantriXahoiSpider(scrapy.Spider):
    name = 'dantri'
    allowed_domains = ['dantri.com.vn']
    start_urls = ['https://dantri.com.vn/xa-hoi.htm', \
                'https://dantri.com.vn/the-gioi.htm',\
                'https://dantri.com.vn/the-thao.htm',\
                'https://dantri.com.vn/giao-duc-khuyen-hoc.htm',\
                'https://dantri.com.vn/tam-long-nhan-ai.htm',\
                'https://dantri.com.vn/kinh-doanh.htm',\
                'https://dantri.com.vn/bat-dong-san.htm',\
                'https://dantri.com.vn/van-hoa.htm',\
                'https://dantri.com.vn/giai-tri.htm',\
                'https://dantri.com.vn/phap-luat.htm',\
                'https://dantri.com.vn/nhip-song-tre.htm',\
                'https://dantri.com.vn/suc-khoe.htm',\
                'https://dantri.com.vn/suc-manh-so.htm',\
                'https://dantri.com.vn/o-to-xe-may.htm',\
                'https://dantri.com.vn/tinh-yeu-gioi-tinh.htm']
    base_url = 'https://dantri.com.vn' 

    def parse(self, response):
        urls = response.css(".icon-detail.fon7::attr(href)").getall()[1:]
        for url in urls:
            url = self.base_url + url
            url = response.urljoin(url)
            # print(url)
            # print("9"*100)
            yield scrapy.Request(url=url, callback=self.parse_news)
        next_page = response.css(".fon27.mt1.mr2::attr(href)").get()
        # print("hehe"*100)
        # print(next_page)
        # print("hehe"*100)
        if next_page:
            # print("haha"*50)
            yield scrapy.Request(self.base_url + next_page, callback=self.parse)
    def parse_news(self, response):
        # print("89"*100)
        link = response.request.url
        title = response.css(".fon31.mgb15::text").get()
        title1_tmp = response.css(".fon33.mt1.sapo::text").getall()
        title1 = ''
        for t in title1_tmp:
            title1 += t
        content_tmp = response.xpath('//*[@id="divNewsContent"]/p//text()').getall()[0:-1]
        content = ''
        for c in content_tmp:
            content += c
        author = response.xpath('//*[@id="divNewsContent"]/p//text()').getall()[-1]
        topic = link[22:link.rfind('/')]
        datetime_news = response.css(".fr.fon7.mr2.tt-capitalize::text").get()
        tags = response.css('.news-tags-item a::attr(title)').getall()
        datetime_crawl = datetime.datetime.now()
        item = {
            'link': link,
            'title': title,
            'title1': title1,
            'content': content,
            'author': author,
            'topic': topic,
            'tags':tags,
            'datetime': datetime_news,
            'datetime_crawl': datetime_crawl
        }
        yield item

        
