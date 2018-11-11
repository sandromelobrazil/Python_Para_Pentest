from scapy.all import *
conf.verb = 0

IPs = []

for ip in range(1, 255):
    IPs.append("192.168.0."+str(ip))

pacoteARP = Ether()/ARP(pdst=IPs, hwdst="ff:ff:ff:ff:ff:ff") #1
ans, unans = srp(pacoteARP, inter=0.1, timeout=1) #2

print "IP\t\tMAC"
for pacoteRecebido in ans:
    print pacoteRecebido[1].psrc, "\t", pacoteRecebido[1].hwsrc #3