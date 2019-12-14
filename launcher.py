#!/usr/local/bin/python
import fire
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from config import Config
import os
from datetime import datetime


class Launcher(object):
    def __init__(self,
                 export=None,
                 obey=None,
                 log_level=None,
                 log=None,
                 useragent=None):
        config = Config()
        self.config_file = config.getConfigFile()
        self.settings = get_project_settings()
        _export = export
        _obey = obey
        _log = log
        _useragent = useragent
        _log_level = log_level

        if isinstance(_log, bool):
            show_log = _log
        else:
            show_log = self.config_file['show_log']

        if show_log is False:
            self.settings['LOG_FILE'] = os.path.join(
                os.path.dirname(os.path.realpath(__file__)), 'log',
                'log-{}.txt'.format(
                    datetime.today().strftime("%A, %d. %B %Y %I:%M%p")))
        else:
            self.settings['LOG_FILE'] = None

        log_levels = ("DEBUG", "INFO", "WARNING", "ERROR")
        if isinstance(_log_level, str) and _log_level in log_levels:
            self.settings['LOG_LEVEL'] = _log_level
        else:
            self.settings['LOG_LEVEL'] = self.config_file['log_level']

        if _export in ('csv', 'json', 'xml'):
            self.settings['FEED_FORMAT'] = _export
        elif self.config_file['export_format']:
            self.settings['FEED_FORMAT'] = self.config_file['export_format']

        if isinstance(_obey, bool):
            self.settings['ROBOTSTXT_OBEY'] = _obey
        elif self.config_file['obey_robots']:
            self.settings['ROBOTSTXT_OBEY'] = self.config_file['obey_robots']

        if isinstance(_useragent, str):
            self.settings['USER_AGENT'] = _useragent

        elif self.config_file['user_agent']:
            self.settings['USER_AGENT'] = self.config_file['user_agent']

        self.process = CrawlerProcess(self.settings)

    def run(self, url):
        '''run spider job'''
        self.process.crawl('checker', url=url)
        return self.process.start()

    def show_config(self):
        '''show defualt configs'''
        for key, value in self.config_file.items():
            print('{} : {}\n'.format(key, value))


if __name__ == '__main__':
    fire.Fire(Launcher)
