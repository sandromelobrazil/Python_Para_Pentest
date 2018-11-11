import ctypes, win32security, win32api, ntsecuritycon

processToken = win32security.OpenProcessToken(win32api.GetCurrentProcess(), ntsecuritycon.TOKEN_ADJUST_PRIVILEGES | ntsecuritycon.TOKEN_QUERY) #1
processPrivilegeValue = win32security.LookupPrivilegeValue(None, ntsecuritycon.SE_SHUTDOWN_NAME) #2
win32security.AdjustTokenPrivileges(processToken, 0, [(processPrivilegeValue, ntsecuritycon.SE_PRIVILEGE_ENABLED)]) #3

ctypes.windll.user32.ExitWindowsEx(5,0) #4
ctypes.windll.user32.ExitWindowsEx(6,0) #5
