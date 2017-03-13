from fixture_code import *
from pywinauto.application import Application
from util import *
import time
import pytest


@pytest.mark.callme
def test_callme(get_mock_approvelogin):
    turn_off_autopush()
    app = Application().Start(cmd_line=u'C:\\Users\\login_test\\Desktop\\Release\\Release\\AuthUiTest.exe login_test')
    window = app.Dialog
    window.Wait('ready')

    button = window[u'Call Me']
    button.SetFocus()
    button.Click()

    time.sleep(10)

    contents = open('msgOutput.txt', 'r').readlines()
    return_code = int(contents[0].strip())
    print return_code

    content_lines = len(contents)
    if content_lines == 1:
        return_code = int(contents[0].strip())
        assert return_code == 1
    elif content_lines:
        return_code = int(contents[0].strip())
        return_msg = contents[1].strip()
        print return_code, return_msg
        assert return_code != 1

    app.Kill_()
