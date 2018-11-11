# -*- coding: utf-8 -*-
import socket

FROM = "falso@email.com"
TO = "destinatario@site.com"
DOMINIO = "site.com"

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((DOMINIO,25))

# Imprime o banner
print sock.recv(1024)

#Envia o email falso
sock.send("HELO " + DOMINIO + "\n")
print sock.recv(1024)

sock.send("MAIL FROM: " + FROM + "\n")
print sock.recv(1024)

sock.send("RCPT TO: " + TO + "\n")
print sock.recv(1024)

sock.send("DATA\n")
print sock.recv(1024)

sock.send("""From: %s
To: %s
Subject: Cabeçalho da mensagem
Aqui entra o corpo do email falso (coloque o que você quiser)
Deixe um ponto na próxima linha para indicar o fim do email
.
""" %(FROM, TO) )
print sock.recv(1024)

sock.send("QUIT\n")
print sock.recv(1024)

sock.close()