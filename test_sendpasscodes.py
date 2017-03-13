from fixture_code import *

from pywinauto.application import Application
import time

import pytest

@pytest.mark.skip(reason="not fully implemented")
def test_sendpasscodes(get_mock_happySleep):
    app = Application().Start(cmd_line=u'C:\\Users\\login_test\\Desktop\\Release\\Release\\AuthUiTest.exe login_test')
    window = app.Dialog
    #window.Wait('ready')

    button2 = window.Cancel
    button2.SetFocus()
    button2.Click()

    time.sleep(2)

    button = window.Button4
    button.SetFocus()
    button.Click()

    contents = open('msgOutput.txt', 'r').readlines()
    content_lines = len(contents)
    if content_lines == 1:
        return_code = int(contents[0].strip())
        print return_code
        assert return_code == 1
    elif content_lines:
        return_code = int(contents[0].strip())
        return_msg = contents[1].strip()
        print return_code, return_msg
        assert return_code != 1

    app.Kill_()
