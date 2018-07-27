import scrapy
from scrapy.spiders import SitemapSpider
from scrapy.linkextractors import LinkExtractor
try:
    from urllib.parse import  urljoin
except ImportError:
     from urlparse import  urljoin
from scrapy.http import Request
import sys
from broken_links.items import Link
from config  import Config
EXTENSIONS = {
   'scrapy.extensions.telnet.TelnetConsole': None,
}

class SiteSpider(SitemapSpider):

  config = Config()
  config_file = config.getConfigFile()
  name= 'single_check'
  starting_urls=[]
  for url in  config.getStartingUrls():
    if url.startswith('http://') or url.startswith('https://'):
      starting_urls.append(urljoin(url, '/robots.txt'))

    else :
      url_tmp = 'http://' + url
      starting_urls.append(urljoin(url_tmp, '/robots.txt'))

  sitemap_urls = starting_urls

  sitemap_rules = [('', 'parse_article')]
  handle_httpstatus_list = [404]

  def __init__(self,  *args, **kwargs):
        super(SiteSpider, self).__init__(*args, **kwargs)
        #isCheckSocial = Config.getIgnoreSocial()


  def parse_article(self, response):


    # print('parse_article url:', response.url)


    social_domains = ('buzzfeed.com','facebook.com','vk.com','pinterest.com','twitter.com','instagram.com','tumblr.com')
    links = LinkExtractor(deny_domains=social_domains).extract_links(response)
    for link in links:
      #info = BrokenUrl()
      #info['url'] = link.url

      yield Request(link.url,self.check_if_broken)


  def check_if_broken(self,response):

    error_status = (404,400,405)
    print(response.status)
    if response.status in error_status :
      info = Link()
      info['url'] = response.url
      yield info
