from scapy.all import *
from binascii import a2b_hex, b2a_hex
import subprocess

arquivo_handshake = "pentest.pcap"
ssid = "pentest"
handshake = rdpcap(arquivo_handshake)

Version_802_1X_2001 = "01"
Version_802_1X_2004 = "02"
Type = "03"

apMac = handshake[0].addr3.replace(":", "")
#apMac = a2b_hex(apMac) #1

cliMac = handshake[0].addr1.replace(":", "")
#cliMac = a2b_hex(cliMac) #2

saida = subprocess.Popen("tshark -r %s -T fields -e wlan_rsna_eapol.keydes.nonce -e wlan_rsna_eapol.keydes.mic 2> /dev/null" %arquivo_handshake, shell=True, stdout=subprocess.PIPE)
lista = saida.stdout.read().split()

aNonce = lista[0].replace(":", "")
#aNonce = a2b_hex(aNonce) #3

sNonce = lista[2].replace(":", "")
#sNonce = a2b_hex(sNonce) #4

mic1 = lista[3].replace(":", "")
mic1_null = "0" * len(mic1)
frame802_1 = Version_802_1X_2001 + Type + "%04x"%handshake[1].len + b2a_hex(handshake[1].load)
frame802_1 = frame802_1.replace(mic1, mic1_null)
#data1 = a2b_hex(frame802_1) #5

mic2 = lista[5].replace(":", "")
mic2_null = "0" * len(mic2)
frame802_2 = Version_802_1X_2004 + Type + "%04x"%handshake[2].len + b2a_hex(handshake[2].load)
frame802_2 = frame802_2.replace(mic2, mic2_null)
#data2 = a2b_hex(frame802_2) #6

mic3 = lista[7].replace(":", "")
mic3_null = "0" * len(mic3)
frame802_3 = Version_802_1X_2001 + Type + "%04x"%handshake[3].len + b2a_hex(handshake[3].load)
frame802_3 = frame802_3.replace(mic3, mic3_null)
#data3 = a2b_hex(frame802_3) #7