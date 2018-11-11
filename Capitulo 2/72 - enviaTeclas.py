import win32com.client, win32gui 

shell = win32com.client.Dispatch('WScript.Shell')
shell.AppActivate(win32gui.GetForegroundWindow()) #1
shell.SendKeys("Texto aleatorio")
