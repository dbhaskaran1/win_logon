import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
import ConfigParser
from _winreg import *

cfg = ConfigParser.ConfigParser()
cfg.read('config/win_login.conf')

host = cfg.get('config_controller', 'host')
port = cfg.get('config_controller', 'port')
url_format_string = cfg.get('config_controller', 'url_format')
config_controller_url = url_format_string.format(host, port)

def request_for_config(config_to_load='happyFull.txt'):
    config_req = requests.get(config_controller_url + config_to_load, verify=False)
    return config_req.status_code, config_req.content

def get_reg_value(key_option):
    key = OpenKey(HKEY_LOCAL_MACHINE,r'SOFTWARE\Duo Security\DuoCredProv', 0, KEY_ALL_ACCESS)
    if key_option == 'host_setting':
        host = QueryValueEx(key, "Host")
        return host
    elif key_option == 'auto_push':
        auto_push = QueryValueEx(key, "AutoPush")
        return str(auto_push)
    else:
        raise Exception('key not found')

def set_reg_value(key_option, value):
    key = OpenKey(HKEY_LOCAL_MACHINE,r'SOFTWARE\Duo Security\DuoCredProv', 0, KEY_ALL_ACCESS)
    if key_option == 'host_setting':
        host = QueryValueEx(key, "Host")
        print 'current host ' + str(host)
        SetValueEx(key, "Host", 1, REG_SZ, value)
        CloseKey(key)
    elif key_option == 'auto_push':
        auto_push = QueryValueEx(key, "AutoPush")
        print 'current auto_push ' + str(auto_push)
        SetValueEx(key, "AutoPush", 1, REG_DWORD, value)
        CloseKey(key)
    else:
        raise Exception('key not found')

def turn_off_autopush():
    set_reg_value('auto_push', 0)

def turn_on_autopush():
    set_reg_value('auto_push', 1)

#print get_reg_value('host_setting')
#set_reg_value('host_setting', u'fakeduo.com:5002')
#set_reg_value('host_setting', u'api-94be6215.test.duosecurity.com')
#set_reg_value('auto_push', 0)
#turn_off_autopush()
#turn_on_autopush()
#print get_reg_value('auto_push')

