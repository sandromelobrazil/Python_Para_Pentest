from scapy.all import *
probe_request = {} #1

def probeRequest(pacote):

    if pacote.haslayer(Dot11ProbeReq): #2

        if pacote.info:
            if pacote.addr2 not in probe_request.keys(): #3
                probe_request[pacote.addr2] = set([pacote.info]) #4
                print "MAC do cliente ->", pacote.addr2
                print "ESSID ->", pacote.info
                print

            elif pacote.info not in probe_request[pacote.addr2]: #5
                probe_request[pacote.addr2].add(pacote.info) #6
                print "MAC do cliente ->", pacote.addr2
                print "ESSID ->", pacote.info
                print

sniff(iface="mon0", prn=probeRequest)