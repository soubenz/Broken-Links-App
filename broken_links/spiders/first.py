import scrapy
from scrapy.spiders import SitemapSpider
from scrapy.linkextractors import LinkExtractor
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from scrapy.http import Request
import sys
from broken_links.items import Link
EXTENSIONS = {
   'scrapy.extensions.telnet.TelnetConsole': None,
}
 
class SiteSpider(SitemapSpider):

  name= 'sou'

  def __init__(self, isCheckSocial, *args, **kwargs):
        super(MySpider, self).__init__(*args, **kwargs)
        
  sitemap_urls = ['http://www.digitbin.com/sitemap_index.xml']

  sitemap_rules = [('', 'parse_article')]
  handle_httpstatus_list = [404]
  
  def parse_article(self, response):


    # print('parse_article url:', response.url)
#domains =

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

 

   
