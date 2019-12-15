import pytest
from launcher import Launcher


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
