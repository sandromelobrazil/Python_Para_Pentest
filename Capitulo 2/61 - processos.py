import wmi

proc = wmi.WMI()
for processo in proc.Win32_Process():
    print processo.ProcessId, "\t", processo.Name