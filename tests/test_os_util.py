from empire.commons.os_util import os_name_OLD


def test_os_name():
    assert os_name_OLD() == "windows"
