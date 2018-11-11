from scapy.all import *
probe_response = {}

def probeResponse(pacote):

    if pacote.haslayer(Dot11ProbeResp):

        if pacote.info:
            if pacote.addr1 not in probe_response.keys():
                probe_response[pacote.addr1] = set([pacote.info])
                print "BSSID ->", pacote.addr2 #1
                print "MAC do cliente ->", pacote.addr1 #2
                print "ESSID ->", pacote.info
                print

            elif pacote.info not in probe_response[pacote.addr1]:
                probe_response[pacote.addr1].add(pacote.info)
                print "BSSID ->", pacote.addr2
                print "MAC do cliente ->", pacote.addr1
                print "ESSID ->", pacote.info
                print

sniff(iface="mon0", prn=probeResponse)