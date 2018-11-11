import socket

host = "site.com"

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((host, 80))
sock.send("HEAD / HTTP/1.1\r\nHost:%s\r\n\r\n" %host) #1
print sock.recv(1024)