#!/usr/bin/env python
# -*- coding: utf-8 -*-

import scrapy
from broken_links.items import Link
from config import Config
from scrapy.http import Request
from scrapy.linkextractors import LinkExtractor
from scrapy.shell import inspect_response
from scrapy.spiders import SitemapSpider
from scrapy.utils.sitemap import Sitemap

try:
    from urllib.parse import urljoin
except ImportError:
    from urlparse import urljoin


class CheckerCore(scrapy.Spider):
    config = Config()
    config_file = config.getConfigFile()
    name = 'checker'
    handle_httpstatus_list = [404, 400, 405]

    def __init__(self, url=None, user_agent=None, *args, **kwargs):
        super(CheckerCore, self).__init__(*args, **kwargs)
        if url.startswith('http://') or url.startswith('https://'):
            url = urljoin(url, '/sitemap.xml')
        else:
            url_tmp = 'http://' + url
            url = urljoin(url_tmp, '/sitemap.xml')

        self.url = url
        self.position = 0

    def start_requests(self):
        yield Request(self.url, callback=self.parse_sitemap)

    def parse_sitemap(self, response):
        sitemap = Sitemap(response.body)
        for site_url in sitemap:
            url = site_url['loc']
            if "sitemap" in url or ".xml" in url:
                yield Request(url, self.parse_sitemap)

            else:
                yield Request(url, self.parse_article)

    def parse_article(self, response):
        social_domains = ('buzzfeed.com', 'facebook.com', 'vk.com',
                          'pinterest.com', 'twitter.com', 'instagram.com',
                          'tumblr.com')
        links = LinkExtractor(
            deny_domains=social_domains).extract_links(response)
        for link in links:
            if not (link.url.startswith('http://')
                    or link.url.startswith('https://')):
                info = Link()
                self.position += 1
                info['position'] = self.position
                info['url'] = link.url
                info['webpage'] = response.url
                yield info
            else:
                yield Request(link.url,
                              self.check_if_broken,
                              meta={"webpage": response.url},
                              errback=lambda x: self.download_errback(
                                  x, link.url, response.url))

    def check_if_broken(self, response):
        webpage = response.meta['webpage']
        error_status = (404, 400, 405)
        if response.status in error_status:
            info = Link()
            self.position += 1
            info['position'] = self.position
            info['url'] = response.url
            info['webpage'] = webpage
            yield info

    def download_errback(self, e, url, current_url):
        info = Link()
        self.position += 1
        info['position'] = self.position
        info['url'] = url
        info['webpage'] = current_url
        yield info
