import hmac
from binascii import a2b_hex, b2a_hex
from hashlib import pbkdf2_hmac, sha1, md5
 
def PRF(key, A, B):
    nByte = 64
    i = 0
    R = b''
    while(i <= ((nByte * 8 + 159) / 160)):
        hmacsha1 = hmac.new(key, A + chr(0x00).encode() + B + chr(i).encode(), sha1)
        R = R + hmacsha1.digest()
        i += 1
    return R[0:nByte]
 
def MakeAB(aNonce, sNonce, apMac, cliMac):
    A = b"Pairwise key expansion"
    B = min(apMac, cliMac) + max(apMac, cliMac) + min(aNonce, sNonce) + max(aNonce, sNonce)
    return (A, B)
 
def MakeMIC(pwd, ssid, A, B, data, wpa = False):
    pmk = pbkdf2_hmac('sha1', pwd.encode('ascii'), ssid.encode('ascii'), 4096, 32)
    ptk = PRF(pmk, A, B)
    hmacFunc = md5 if wpa else sha1
    mics = [hmac.new(ptk[0:16], i, hmacFunc).digest() for i in data]
    return (mics, ptk, pmk)

#def RunTest(psk, ssid, aNonce, sNonce, apMac, cliMac, \
#            frame802_1, frame802_2, frame802_3, mic1, mic2, mic3):
def RunTest(psk):

    #apMac = a2b_hex(apMac)
    #cliMac = a2b_hex(cliMac)
    #aNonce = a2b_hex(aNonce)
    #sNonce = a2b_hex(sNonce)
    #data1 = a2b_hex(frame802_1)
    #data2 = a2b_hex(frame802_2)
    #data3 = a2b_hex(frame802_3)

    #Create parameters for the creation of the PTK, PMK, and MICs
    A, B = MakeAB(aNonce, sNonce, apMac, cliMac)
    #Generate the MICs, the PTK, and the PMK
    mics, ptk, pmk = MakeMIC(psk, ssid, A, B, [data1, data2, data3])
    #Display the pairwise master key (PMK)
    pmkStr = b2a_hex(pmk).decode().upper()
    #print("pmk:\t\t" + pmkStr + '\n')
    #Display the pairwise transient key (PTK)
    ptkStr = b2a_hex(ptk).decode().upper()
    #print("ptk:\t\t" + ptkStr + '\n')
    #Display the desired MIC1 and compare to target MIC1
    mic1Str = mic1.upper()
    #print("desired mic:\t" + mic1Str)
    #Take the first 128-bits of the 160-bit SHA1 hash
    micStr = b2a_hex(mics[0]).decode().upper()[:-8]
    #print("actual mic:\t" + micStr)
    #print('MATCH\n' if micStr == mic1Str else 'MISMATCH\n')
    #Display the desired MIC2 and compare to target MIC2
    mic2Str = mic2.upper()
    #print("desired mic:\t" + mic2Str)
    #Take the first 128-bits of the 160-bit SHA1 hash
    micStr = b2a_hex(mics[1]).decode().upper()[:-8]
    #print("actual mic:\t" + micStr)
    #print('MATCH\n' if micStr == mic2Str else 'MISMATCH\n')
    #Display the desired MIC3 and compare to target MIC3
    mic3Str = mic3.upper()
    #print("desired mic:\t" + mic3Str)
    #Take the first 128-bits of the 160-bit SHA1 hash
    micStr = b2a_hex(mics[2]).decode().upper()[:-8]
    #print("actual mic:\t" + micStr)
    #print('MATCH\n' if micStr == mic3Str else 'MISMATCH\n')
    if micStr == mic3Str:
        return psk
    else:
        return False

def info(ssid_, aNonce_, sNonce_, apMac_, cliMac_, \
         frame802_1_, frame802_2_, frame802_3_, mic1_, mic2_, mic3_):
    global ssid, aNonce, sNonce, apMac, cliMac, data1, data2, data3, mic1, mic2, mic3
    ssid = ssid_
    aNonce = a2b_hex(aNonce_)
    sNonce = a2b_hex(sNonce_)
    apMac = a2b_hex(apMac_)
    cliMac = a2b_hex(cliMac_)
    data1 = a2b_hex(frame802_1_)
    data2 = a2b_hex(frame802_2_)
    data3 = a2b_hex(frame802_3_)
    mic1 = mic1_
    mic3 = mic2_
    mic3 = mic3_

ssid, aNonce, sNonce, apMac, cliMac = "", "", "", "", "" #1
data1, data2, data3 = "", "", "" #2
mic1, mic2, mic3 = "", "", "" #3