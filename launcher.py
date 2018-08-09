#!/usr/local/bin/python
import fire
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from config  import Config
import os
from datetime import datetime

class Launcher(object):

    def __init__(self, export=None, obey=None, log=None):
        # self.list = args
        config = Config()

        self.config_file = config.getConfigFile()
        self.settings = get_project_settings()
        _export = export
        _obey = obey
        _log = log

        if isinstance(_log, bool):
            show_log = _log

        else :
            show_log = self.config_file['show_log']

        if show_log is False:
            self.settings['LOG_FILE'] = os.path.join(os.path.dirname(os.path.realpath(__file__)),'log')+'/log - {}.txt'.format(datetime.today().strftime("%A, %d. %B %Y %I:%M%p"))
        else :
            self.settings['LOG_FILE'] = None

        if _export in ('csv','json','xml'):
            self.settings['FEED_FORMAT'] = _export

        elif self.config_file['export_format']:
            self.settings['FEED_FORMAT'] = self.config_file['export_format']


        if isinstance(_obey, bool):
            self.settings['ROBOTSTXT_OBEY'] = _obey

        elif self.config_file['obey_robots']:
            self.settings['ROBOTSTXT_OBEY'] = self.config_file['obey_robots']
        self.process = CrawlerProcess(self.settings)


    def run(self, url):
        self.process.crawl('sitemap_spider', url=url)
        return self.process.start()


    def show_config(self):
        'show defualt configs'
        for key, value in self.config_file.iteritems():
            print('{} : {}\n'.format(key, value))

if __name__ == '__main__':
  fire.Fire(Launcher)
