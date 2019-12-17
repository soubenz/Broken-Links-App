from pprint import pprint

import scrapy
from scrapy.http import Request
from scrapy.linkextractors import LinkExtractor
from scrapy.utils.sitemap import Sitemap

from broken_links_app.config.config import Config
from broken_links_app.items import Link

try:
    from urllib.parse import urljoin
except ImportError:
    from urlparse import urljoin


class CheckerCore(scrapy.Spider):
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
        pprint('start scanning ...')
        yield Request(self.url, callback=self.parse_sitemap)

    def parse_sitemap(self, response):
        sitemap = Sitemap(response.body)
        for site_url in sitemap:
            url = site_url['loc']
            if "sitemap" in url and ".xml" in url:
                yield Request(url, self.parse_sitemap)

            else:
                yield Request(url, self.parse_page)

    def parse_page(self, response):
        social_domains = Config.social_domains
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
                info['reason'] = 'no schema'
                pprint(
                    f"found broken link # {info['position']}: {info['url']}")
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
            info['reason'] = response.status
            pprint(f"found broken link # {info['position']}: {info['url']}")
            yield info

    def download_errback(self, e, url, current_url):
        info = Link()
        self.position += 1
        info['position'] = self.position
        info['url'] = url
        info['webpage'] = current_url
        info['reason'] = str(e)
        pprint(f"found broken link # {info['position']}: {info['url']}")
        yield info
