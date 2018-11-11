import _winreg

UACKey = _winreg.OpenKey(_winreg.HKEY_LOCAL_MACHINE,
                         'SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Policies\\System',
                         0, _winreg.KEY_ALL_ACCESS)

_winreg.SetValueEx(UACKey, 'EnableLUA', 0, _winreg.REG_DWORD, 0) #1
_winreg.CloseKey(UACKey)