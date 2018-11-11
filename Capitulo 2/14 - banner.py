import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(("localhost", 22)) #1
print sock.recv(2048) #2
sock.close() #3