from fixture_code import *
from pywinauto.application import Application
from util import *
import time
import pytest

@pytest.mark.push
def test_cancel_selectphone_sendpush(get_mock_cancelpush):
    '''
    With autopush enabled, we launch the app, cancel the auto push in progress,select a different phone and send a push
    '''
    turn_on_autopush()
    app = Application().Start(cmd_line=u'C:\\Users\\login_test\\Desktop\\Release\\Release\\AuthUiTest.exe login_test')
    window = app.Dialog
    window.Wait('ready')

    button2 = window.Cancel
    button2.SetFocus()
    button2.Click()

    combobox = window.ComboBox
    combobox.Select(u'Android (XXX-XXX-4349)')
    button = window.Button
    button.Click()

    time.sleep(10)
    app.Kill_()

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

@pytest.mark.push
def test_sendpush(get_mock_happySleep):
    turn_on_autopush()
    app = Application().Start(cmd_line=u'C:\\Users\\login_test\\Desktop\\Release\\Release\\AuthUiTest.exe login_test')
    window = app.Dialog
    window.Wait('ready')

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
