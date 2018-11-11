import win32process, win32gui, win32com.client

janelas = {} #1

def enumeraJanelas(hwnd, lParam):
    if win32gui.IsWindowVisible(hwnd) and win32gui.GetWindowText(hwnd): #2
        PID = win32process.GetWindowThreadProcessId(hwnd)[1]
        janelas[PID] = win32gui.GetWindowText(hwnd)

win32gui.EnumWindows(enumeraJanelas, None) #3

print "PID\tJanela"
for PID in janelas:
    print PID, "\t", janelas[PID]

PID = input("Digite o PID: ")
shell = win32com.client.Dispatch('WScript.Shell') #4
shell.AppActivate(PID) #5