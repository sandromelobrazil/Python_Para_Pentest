from scapy.all import *

handshakes = {}

def captura_4_way(pacote):

    if pacote.haslayer(EAPOL): #1
        if pacote.addr1 != pacote.addr3: #2
            try:
                handshakes[pacote.addr1].append(pacote) #3
            except:
                handshakes[pacote.addr1] = list(pacote) #4

        elif pacote.addr1 == pacote.addr3: #5
            handshakes[pacote.addr2].append(pacote) #6
            if len(handshakes[pacote.addr2]) == 4: #7
                wrpcap("%s.pcap" %pacote.addr3, handshakes[pacote.addr2]) #8
                del handshakes[pacote.addr2] #9
                print "4-way handshake capturado para o BSSID %s" %pacote.addr3

print "Aguardando o 4-way handshake"
sniff(iface="mon0", prn=captura_4_way)