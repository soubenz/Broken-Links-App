from fire import Fire
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from config.config import Config
import os
from datetime import datetime


class Launcher(object):
    def __init__(self,
                 export=None,
                 obey=None,
                 log_level=None,
                 debug=None,
                 useragent=None):
        conf = Config()
        self.conff = conf.getConfigFile()
        self.settings = get_project_settings()
        _export = export
        _obey = obey
        _debug = debug
        _useragent = useragent
        _log_level = log_level

        debug = _debug if isinstance(_debug, bool) else self.conff['debug']

        self.settings['LOG_FILE'] = None
        f_date = datetime.today().strftime("%d_%m_%y.%I.%M")
        if not debug:
            self.settings['LOG_FILE'] = os.path.join(
                os.path.dirname(os.path.realpath(__file__)), 'log',
                f'-{f_date}.txt')

        log_levels = ("DEBUG", "INFO", "WARNING", "ERROR")
        if isinstance(_log_level, str) and _log_level in log_levels:
            self.settings['LOG_LEVEL'] = _log_level
        else:
            self.settings['LOG_LEVEL'] = self.conff['log_level']

        if _export in ('csv', 'json', 'xml'):
            export_format = _export
        elif self.conff['export_format']:
            export_format = self.conff['export_format']
        self.settings['FEED_FORMAT'] = export_format
        self.settings['FEED_URI'] = f'export{f_date}.{export_format}'

        self.settings.update(
            self._set_setting(self.conff, {
                "ROBOTSTXT_OBEY": _obey,
                "USER_AGENT": _useragent,
            }))

        self.process = CrawlerProcess(self.settings)

    def run(self, url):
        '''run spider job'''
        self.process.crawl('checker', url=url)
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
