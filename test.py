
#!/usr/local/bin/python
import fire
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
# from thread import MyThread, WebCrawler
from config  import Config

class BrokenCalculator(object):

    def __init__(self, ignore_social=True):
        # self.list = args
        
        self.process = CrawlerProcess(get_project_settings())
        self._offset = offset

    def add(self, url):

        # for arg in args:
        self.process.crawl('single_check')
        return self
        # self.process.start()
    # return x + y + self._offset

    def add2(self):
        return  self.process.crawl('single_check')
    # return x * y + self._offset
    def run(self):
        return self.process.start()
        pass

if __name__ == '__main__':
  fire.Fire(BrokenCalculator)


# process = CrawlerProcess(get_project_settings())

# process.crawl('single_check')
# process.start()
