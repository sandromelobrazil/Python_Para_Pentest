#Adaptacao: https://stackoverflow.com/questions/3050262/change-browser-proxy-settings-from-python
import _winreg

INTERNET_SETTINGS = _winreg.OpenKey(_winreg.HKEY_CURRENT_USER,
    r'Software\Microsoft\Windows\CurrentVersion\Internet Settings',
    0, _winreg.KEY_ALL_ACCESS) #1

def set_key(name, value, type): #2
    _winreg.SetValueEx(INTERNET_SETTINGS, name, 0, type, value)

set_key('ProxyEnable', 1, _winreg.REG_DWORD) #3
set_key('ProxyOverride', u'localhost; 192.168.0.*', _winreg.REG_SZ) #4
set_key('ProxyServer', u'localhost:8080', _winreg.REG_SZ) #5

import ctypes #6
internet_set_option = ctypes.windll.Wininet.InternetSetOptionW
internet_set_option(0, 37, 0, 0)
internet_set_option(0, 39, 0, 0)