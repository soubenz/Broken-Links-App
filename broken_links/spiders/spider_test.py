#!/usr/bin/env python
# -*- coding: utf-8 -*-

import scrapy
from scrapy.spiders import SitemapSpider
from scrapy.utils.sitemap import Sitemap
from scrapy.linkextractors import LinkExtractor
try:
    from urllib.parse import  urljoin
except ImportError:
     from urlparse import  urljoin
from scrapy.http import Request
import sys
from broken_links.items import Link
from config  import Config
import re
from scrapy.shell import inspect_response

from scrapy.http import Request
# from Amazon_ML_v2.items import CrawlingItem


class AmazonSpider(scrapy.Spider):
    config = Config()
    config_file = config.getConfigFile()
    name= 'test'

    handle_httpstatus_list = [404,400,405]



    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.117 Safari/537.36',
    }


    def __init__(self, crawlID=None,url = None , *args, **kwargs):
        super(AmazonSpider, self).__init__(*args, **kwargs)
        # Load configs amazon
        self.domain = url
          # for url in  config.getStartingUrls():
        if url.startswith('http://') or url.startswith('https://'):
            url =urljoin(url, '/sitemap.xml')

        else :
            url_tmp = 'http://' + url
            url= urljoin(url_tmp, '/sitemap.xml')

        self.url = url

    def start_requests(self):
        yield Request(self.url, callback=self.parse_sitemap,headers= self.headers)

    def parse_sitemap(self, response):
        sitemap = Sitemap(response.body)
        for site_url in sitemap:
            url = site_url['loc']
            if "sitemap" in url or ".xml" in url:
                yield Request(url,self.parse_sitemap )

            else :
                yield Request(url,self.parse_article, headers= self.headers)

    def parse_article(self, response):
    #
    #
    #     # print('parse_article url:', response.url)
    #
    #
        social_domains = ('buzzfeed.com','facebook.com','vk.com','pinterest.com','twitter.com','instagram.com','tumblr.com')
        links = LinkExtractor(deny_domains=social_domains).extract_links(response)
        for link in links:
          #info = BrokenUrl()
          #info['url'] = link.url

          # yield Request(link.url,self.check_if_broken, meta={"webpage":response.url} )
          yield Request(link.url,self.check_if_broken, meta={"webpage":response.url}, errback = lambda x: self.download_errback(x, link.url, response.url))


    #
    # def parse_robots_file(self, response):
    #     text = response.body.split('\n')
    #     for rule in text:
    #         match = re.findall()

    def check_if_broken(self,response):
        webpage = response.meta['webpage']
        error_status = (404,400,405)
        print(response.status)
        if response.status in error_status :
            info = Link()
            info['url'] = response.url
            info['webpage'] = webpage

            yield info


    def download_errback(self, e, url, current_url):
        self.logger.info('++++++++'+ url)
        info = Link()
        info['url'] = url
        info['webpage'] = current_url
        yield info
        # print url
