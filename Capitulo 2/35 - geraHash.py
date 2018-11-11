#Fonte: https://www.trustedsec.com/2010/03/generate-an-ntlm-hash-in-3-lines-of-python
import hashlib,binascii

hash = hashlib.new('md4', "moreno".encode('utf-16le')).digest()
print binascii.hexlify(hash)