import time,msfrpc

client = msfrpc.Msfrpc({}) #1
client.login("msf", "senha_secreta") #2
sessao = client.call("console.create") #3

comando = """use auxiliary/scanner/smb/smb_version
set RHOSTS 192.168.0.2
exploit
""" #4

client.call("console.write", [sessao["id"], comando]) #5
time.sleep(1) #6
resultado = client.call("console.read", [ sessao["id"] ]) #7

while resultado["busy"]: #8
    resultado = client.call("console.read", [ sessao["id"] ]) #9
    time.sleep(1) #10

print resultado["data"] #11
client.call("console.destroy", [sessao["id"]]) #12