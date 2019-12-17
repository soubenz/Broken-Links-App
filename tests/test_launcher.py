import pytest
from . import Launcher
from scrapy.spiders import Spider
from scrapy.crawler import CrawlerRunner
from broken_links_app.spiders.spider import CheckerCore
from pathlib import Path
from datetime import datetime


def test_set_settings():
    config = {"k": True, "t": None}

    set_dict = {"k": None, "t": False}
    # assert that sets from config file
    assert Launcher._set_setting(config, set_dict)['K'] is True
    # assert that sets from arguments
    assert Launcher._set_setting(config, set_dict)['T'] is False


def test_set_settings_named():
    config = {"k": True, "t": None}

    set_dict = {"k": "test", "t": False}
    # to set from config because value isn't in named
    assert Launcher._set_setting(config, set_dict, set("not"))['K'] is True


@pytest.fixture
def _run_crawler():
    """
    spider_cls: Scrapy Spider class
    settings: Scrapy settings
    returns: Twisted Deferred
    """
    launcher = Launcher()
    runner = CrawlerRunner(launcher.settings)
    return runner


def test_scrapy_crawler(_run_crawler):
    launcher = Launcher()
    print(launcher.settings)
    runner = _run_crawler
    deferred = runner.crawl(CheckerCore, url="http://httpbin.org")
    # inspired by https://stackoverflow.com/questions/48913525/scrapy-raises-reactornotrestartable-when-crawlerprocess-is-ran-twice

    @deferred.addCallback
    def _success(results):
        f_date = datetime.today().strftime("%d_%m_%y.%I.%M")
        p_export = Path(
            launcher.conff['export_dir']) / 'export' / f'{f_date}.csv'
        assert True
        assert p_export.exists()

    @deferred.addErrback
    def _error(failure):
        raise failure.value

    return deferred
