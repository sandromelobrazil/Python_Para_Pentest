import pythoncom, pyHook

def StopKeys(event):
    teclas = ["a", "b", "c"]
    if chr(event.Ascii) in teclas:
        return False
    else:
        return True

hm=pyHook.HookManager()
hm.KeyAll = StopKeys
hm.HookKeyboard()
pythoncom.PumpMessages()