from fire import Fire
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from broken_links_app.config.config import Config
from broken_links_app.spiders.spider import CheckerCore
import os
from datetime import datetime
from pathlib import Path


class Launcher(object):
    def __init__(self,
                 export=None,
                 obey=None,
                 log_level=None,
                 debug=None,
                 log_dir=None,
                 export_dir=None,
                 useragent=None):
        conf = Config()
        self.conff = conf.getConfigFile()
        self.settings = get_project_settings()
        _export = export
        _obey = obey
        _debug = debug
        _useragent = useragent
        _log_level = log_level
        _export_dir = export_dir
        _log_dir = log_dir

        debug = _debug if isinstance(_debug, bool) else self.conff['debug']
        export_dir = _export_dir if isinstance(
            _debug, str) else self.conff['export_dir']
        log_dir = _log_dir if isinstance(_log_dir,
                                         str) else self.conff['log_dir']

        self.settings['LOG_FILE'] = None
        f_date = datetime.today().strftime("%d_%m_%y.%I.%M")
        if not debug:
            p_log = Path(log_dir) / 'log' / f'{f_date}.txt'
            self.settings['LOG_FILE'] = p_log

        log_levels = ("DEBUG", "INFO", "WARNING", "ERROR")
        if isinstance(_log_level, str) and _log_level in log_levels:
            self.settings['LOG_LEVEL'] = log_level
        else:
            self.settings['LOG_LEVEL'] = self.conff['log_level']

        if _export in ('csv', 'json', 'xml'):
            export_format = _export
        elif self.conff['export_format']:
            export_format = self.conff['export_format']
        self.settings['FEED_FORMAT'] = export_format
        p = Path(export_dir) / 'export' / f'{f_date}.{export_format}'
        self.settings['FEED_URI'] = p.as_uri()

        self.settings.update(
            self._set_setting(self.conff, {
                "ROBOTSTXT_OBEY": _obey,
                "USER_AGENT": _useragent,
            }))

    def run(self, url):
        '''run spider job'''
        self.process = CrawlerProcess(self.settings)
        self.process.crawl(CheckerCore, url=url)
        return self.process.start()

    def show_config(self):
        '''show defualt configs'''
        for key, value in self.conff.items():
            print('{} : {}\n'.format(key, value))

    @staticmethod
    def _set_setting(config, kw, named=set()):
        settings = {}
        for k, v in kw.items():
            if not named:
                named.add(v)
            if v is not None and v in named:
                settings[k.upper()] = v

            elif k in config:
                settings[k.upper()] = config[k]
            named.clear()
        return settings


if __name__ == '__main__':
    Fire(Launcher)
