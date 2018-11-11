import socket

host = "localhost"
portas = [21,22,23,80]

print "Portas abertas"
for porta in portas:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #1
    sock.settimeout(1) #2
    codigoRetorno = sock.connect_ex((host, porta)) #3
    sock.close() #4
    if codigoRetorno == 0: #5
        print porta