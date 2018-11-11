import hashlib,binascii

usuario = "daniel" #1
hashMimikatz = "59e12999a1fc4ccec8d30dfe860b65b7" #2

with open("lista.txt", "r") as lista: #3
    while True: #4
        senha = lista.readline().strip("\n") #5
        if not senha: #6
            break

        hash = hashlib.new('md4', senha.encode('utf-16le')).digest() #7

        if binascii.hexlify(hash) == hashMimikatz: #8
            print "USER \t", usuario #9
            print "PASS \t", senha
            print "HASH \t", binascii.hexlify(hash) 
            break