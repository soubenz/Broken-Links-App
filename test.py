#!/usr/local/bin/python
import fire
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from config  import Config
import os
from datetime import datetime
class Launcher(object):

    def __init__(self, ignore_social=True):
        # self.list = args
        config = Config()

        self.config_file = config.getConfigFile()
        settings = get_project_settings()
        if os.path.exists(os.path.dirname(os.path.realpath(__file__))+'/__configs.ini'):
            data = ConfigObj(os.path.dirname(os.path.realpath(__file__))+'/__configs.ini')

        if self.config_file['show_log'] is False:
            settings['LOG_FILE'] = os.path.join(os.path.dirname(os.path.realpath(__file__)),'log')+'/log - {}.txt'.format(datetime.today().strftime("%A, %d. %B %Y %I:%M%p"))
        else :
            settings['LOG_FILE'] = None
        self.process = CrawlerProcess(settings)

    def run(self, url):

        # for arg in args:
        self.process.crawl('sitemap_spider', url=url)
        return self.process.start()
        # return self
        # self.process.start()
    # return x + y + self._offset


if __name__ == '__main__':
  fire.Fire(Launcher)


# process = CrawlerProcess(get_project_settings())

# process.crawl('single_check')
# process.start()
