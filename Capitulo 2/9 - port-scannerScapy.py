from scapy.all import *
conf.verb = 0 #1

portas = [21,22,23,80,8080]

pacoteIP = IP(dst ="IP do destino")
pacoteTCP = TCP(dport=portas, flags="S")
pacote = pacoteIP/pacoteTCP

ans, unans = sr(pacote, inter=0.1, timeout=1) #2

print "Porta\tEstado"
for pacoteRecebido in ans:
    print pacoteRecebido[1][IP].sport, \
    "\t", pacoteRecebido[1][TCP].sprintf("%flags%") #3
