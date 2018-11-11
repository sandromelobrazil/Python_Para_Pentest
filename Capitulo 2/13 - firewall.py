from scapy.all import *
conf.verb = 0

host = "IP do destino"
portas = [22,80,666,12345]

pacote = IP(dst=host) / TCP(dport=portas, flags="S")
ans, unans = sr(pacote, inter=0.1, timeout=1)

print "PORTA\tESTADO"
for pacoteRecebido in ans: #1
    if pacoteRecebido[1].haslayer("ICMP"): #2
        if pacoteRecebido[1]["ICMP"].type == 3 \
        and pacoteRecebido[1]["ICMP"].code == 3: #3
            print pacoteRecebido[0][TCP].dport , "\tREJECT" #4
    elif pacoteRecebido[1].haslayer("TCP"): #5
        print pacoteRecebido[1][TCP].sport, "\t", \
        pacoteRecebido[1][TCP].sprintf("%flags%") #6

for pacoteNaoRecebido in unans: #7
    print pacoteNaoRecebido.dport, "\tDROP"