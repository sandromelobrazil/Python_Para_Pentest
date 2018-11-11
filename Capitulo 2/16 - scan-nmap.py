import nmap

scanNmap = nmap.PortScanner() #1
scanNmap.scan("192.168.0.1", "22,80") #2

print "Valores de scanNmap['192.168.0.1']"
print scanNmap["192.168.0.1"] #3

print "-" * 40 

print "Chaves do dicionario scanNmap['192.168.0.1']"
for valores in scanNmap["192.168.0.1"]: #4
    print valores

print "-" * 40

print "Valores de scanNmap['192.168.0.1']['status']"
print scanNmap["192.168.0.1"]["status"] #5

print "-" * 40

print "Valor de scanNmap ['192.168.0.1']['status']['state']"
print scanNmap["192.168.0.1"]["status"]["state"] #6