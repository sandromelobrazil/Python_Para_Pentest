# -*- coding: utf-8 -*-
import nmap

scanNmap = nmap.PortScanner()
scanNmap.scan("192.168.0.1 192.168.0.2", "22,80")

# Parâmetros do Nmap podem ser inseridos como terceiro argumento. Exemplo:
#scanNmap.scan("192.168.0.1 192.168.0.2", "22,80", "-sS -O")
# Outra forma
#scanNmap.scan("192.168.0.1 192.168.0.2", arguments="-p22,80 -sS -O")

# Descomente a linha a seguir para saber qual foi a linha de comando usada para o escaneamento
#print scanNmap.command_line()

for host in scanNmap.all_hosts(): #1
    print "Nmap scan report for", host
    print "Host is", scanNmap[host]["status"]["state"] #2

    for protocolo in scanNmap[host].all_protocols(): #3
        print "PORT\tSTATE\tSERVICE"
        for porta in scanNmap[host][protocolo]: #4
            alvo = scanNmap[host][protocolo][porta] #5
            print str(porta) + "/" + protocolo + "\t" + \
            alvo["state"] + "\t" + alvo["name"] #6

    enderecoMAC = scanNmap[host]["addresses"]["mac"]
    print "MAC Address: " + enderecoMAC + " (" + \
    scanNmap[host]["vendor"][enderecoMAC] + ")" + "\n" #7