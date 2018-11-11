from scapy.all import *
import threading, subprocess, time

BSSIDs = []

def sniffer_beacon(pacote):
    if pacote.haslayer(Dot11): #1
        if pacote.type == 0 and pacote.subtype == 8: #2
            if pacote.addr2 not in BSSIDs: #3
                print "ESSID ->", pacote.info #4
                print "BSSID ->", pacote.addr2 #5
                print "Canal ->", ord(pacote[Dot11Elt:3].info) #6
                print
                BSSIDs.append(pacote.addr2) #7

def varre_canais(): #8
    while True:
        for canal in range(1,14):
            subprocess.Popen("iwconfig mon0 channel %d" %canal, shell=True)
            time.sleep(3)
threading.Thread(target=varre_canais).start()

sniff(iface="mon0", prn= sniffer_beacon)