import pytest
from util import *

@pytest.fixture
def get_mock_happySleep():
    config_requested = 'happyFullSleep5.txt'
    (status_code, content) = request_for_config(config_requested)
    expected_content = '{"response":"Test ID: ' + config_requested + ' has been loaded"}'
    print (status_code, content)

@pytest.fixture
def get_mock_cancelpush():
    config_requested = 'cancelSwitchToPushDifferentPhone.txt'
    (status_code, content) = request_for_config(config_requested)
    expected_content = '{"response":"Test ID: ' + config_requested + ' has been loaded"}'
    print (status_code, content)

@pytest.fixture
def get_mock_happyFull():
    config_requested = 'happyFull.txt'
    (status_code, content) = request_for_config(config_requested)
    expected_content = '{"response":"Test ID: ' + config_requested + ' has been loaded"}'
    print (status_code, content)

@pytest.fixture
def get_mock_approvelogin():
    config_requested = 'approveLogin.txt'
    (status_code, content) = request_for_config(config_requested)
    expected_content = '{"response":"Test ID: ' + config_requested + ' has been loaded"}'
    print (status_code, content)
