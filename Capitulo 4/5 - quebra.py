from scapy.all import *
import hmac, subprocess
from binascii import a2b_hex, b2a_hex
from hashlib import pbkdf2_hmac, sha1, md5
 
#Pseudo-random function for generation of
#the pairwise transient key (PTK)
#key:       The PMK
#A:         b'Pairwise key expansion'
#B:         The apMac, cliMac, aNonce, and sNonce concatenated
#           like mac1 mac2 nonce1 nonce2
#           such that mac1 < mac2 and nonce1 < nonce2
#return:    The ptk
def PRF(key, A, B):
    #Number of bytes in the PTK
    nByte = 64
    i = 0
    R = b''
    #Each iteration produces 160-bit value and 512 bits are required
    while(i <= ((nByte * 8 + 159) / 160)):
        hmacsha1 = hmac.new(key, A + chr(0x00).encode() + B + chr(i).encode(), sha1)
        R = R + hmacsha1.digest()
        i += 1
    return R[0:nByte]
 
#Make parameters for the generation of the PTK
#aNonce:        The aNonce from the 4-way handshake
#sNonce:        The sNonce from the 4-way handshake
#apMac:         The MAC address of the access point
#cliMac:        The MAC address of the client
#return:        (A, B) where A and B are parameters
#               for the generation of the PTK
def MakeAB(aNonce, sNonce, apMac, cliMac):
    A = b"Pairwise key expansion"
    B = min(apMac, cliMac) + max(apMac, cliMac) + min(aNonce, sNonce) + max(aNonce, sNonce)
    return (A, B)
 
#Compute the 1st message integrity check for a WPA 4-way handshake
#pwd:       The password to test
#ssid:      The ssid of the AP
#A:         b'Pairwise key expansion'
#B:         The apMac, cliMac, aNonce, and sNonce concatenated
#           like mac1 mac2 nonce1 nonce2
#           such that mac1 < mac2 and nonce1 < nonce2
#data:      A list of 802.1x frames with the MIC field zeroed
#return:    (x, y, z) where x is the mic, y is the PTK, and z is the PMK
def MakeMIC(pwd, ssid, A, B, data, wpa = False):
    #Create the pairwise master key using 4096 iterations of hmac-sha1
    #to generate a 32 byte value
    pmk = pbkdf2_hmac('sha1', pwd.encode('ascii'), ssid.encode('ascii'), 4096, 32)
    #Make the pairwise transient key (PTK)
    ptk = PRF(pmk, A, B)
    #WPA uses md5 to compute the MIC while WPA2 uses sha1
    hmacFunc = md5 if wpa else sha1
    #Create the MICs using HMAC-SHA1 of data and return all computed values
    mics = [hmac.new(ptk[0:16], i, hmacFunc).digest() for i in data]
    return (mics, ptk, pmk)

#Run a brief test showing the computation of the PTK, PMK, and MICS
#for a 4-way handshake
def RunTest():

    #Create parameters for the creation of the PTK, PMK, and MICs
    A, B = MakeAB(aNonce, sNonce, apMac, cliMac)
    #Generate the MICs, the PTK, and the PMK
    mics, ptk, pmk = MakeMIC(psk, ssid, A, B, [data1, data2, data3])
    #Display the pairwise master key (PMK)
    pmkStr = b2a_hex(pmk).decode().upper()
    print("pmk:\t\t" + pmkStr + '\n')
    #Display the pairwise transient key (PTK)
    ptkStr = b2a_hex(ptk).decode().upper()
    print("ptk:\t\t" + ptkStr + '\n')
    #Display the desired MIC1 and compare to target MIC1
    mic1Str = mic1.upper()
    print("desired mic:\t" + mic1Str)
    #Take the first 128-bits of the 160-bit SHA1 hash
    micStr = b2a_hex(mics[0]).decode().upper()[:-8]
    print("actual mic:\t" + micStr)
    print('MATCH\n' if micStr == mic1Str else 'MISMATCH\n')
    #Display the desired MIC2 and compare to target MIC2
    mic2Str = mic2.upper()
    print("desired mic:\t" + mic2Str)
    #Take the first 128-bits of the 160-bit SHA1 hash
    micStr = b2a_hex(mics[1]).decode().upper()[:-8]
    print("actual mic:\t" + micStr)
    print('MATCH\n' if micStr == mic2Str else 'MISMATCH\n')
    #Display the desired MIC3 and compare to target MIC3
    mic3Str = mic3.upper()
    print("desired mic:\t" + mic3Str)
    #Take the first 128-bits of the 160-bit SHA1 hash
    micStr = b2a_hex(mics[2]).decode().upper()[:-8]
    print("actual mic:\t" + micStr)
    print('MATCH\n' if micStr == mic3Str else 'MISMATCH\n')
    return

arquivo_handshake = "pentest.pcap" #1
handshake = rdpcap(arquivo_handshake)

ssid = "pentest" #2
psk = "senha123" #3

Version_802_1X_2001 = "01" #4
Version_802_1X_2004 = "02" #5
Type = "03" #6

apMac = handshake[0].addr3.replace(":", "") #7
apMac = a2b_hex(apMac) #8

cliMac = handshake[0].addr1.replace(":", "") #9
cliMac = a2b_hex(cliMac) #10

saida = subprocess.Popen("tshark -r %s -T fields -e wlan_rsna_eapol.keydes.nonce -e wlan_rsna_eapol.keydes.mic 2> /dev/null" %arquivo_handshake, shell=True, stdout=subprocess.PIPE) #11
lista = saida.stdout.read().split() #12

aNonce = lista[0].replace(":", "") #13
aNonce = a2b_hex(aNonce) #14

sNonce = lista[2].replace(":", "")
sNonce = a2b_hex(sNonce)

mic1 = lista[3].replace(":", "") #15
mic1_null = "0" * len(mic1) #16
frame802_1 = Version_802_1X_2001 + Type + "%04x"%handshake[1].len + b2a_hex(handshake[1].load) #17
frame802_1 = frame802_1.replace(mic1, mic1_null) #18
data1 = a2b_hex(frame802_1) #19


mic2 = lista[5].replace(":", "")
mic2_null = "0" * len(mic2)
frame802_2 = Version_802_1X_2004 + Type + "%04x"%handshake[2].len + b2a_hex(handshake[2].load)
frame802_2 = frame802_2.replace(mic2, mic2_null)
data2 = a2b_hex(frame802_2)


mic3 = lista[7].replace(":", "")
mic3_null = "0" * len(mic3)
frame802_3 = Version_802_1X_2001 + Type + "%04x"%handshake[3].len + b2a_hex(handshake[3].load)
frame802_3 = frame802_3.replace(mic3, mic3_null)
data3 = a2b_hex(frame802_3)


RunTest() #20