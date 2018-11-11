# -*- coding: utf-8 -*-
import socket

usuarios = ["daniel", "teste", "root"]

for usuario in usuarios:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #1
    sock.connect(("IP do servidor SMTP",25)) #2
    sock.recv(1024) #3
    sock.send("VRFY " + usuario + "\n") #4
    resposta = sock.recv(1024) #5
    sock.close() #6
    if "252" in resposta: #7
        print usuario + "-> Válido!"
    elif "550" in resposta:
        print usuario + "-> Usuário não encontrado!"
    elif "503" in resposta:
        print "Servidor requer autenticação"
        break
    elif "500" in resposta:
        print "Comando VRFY não suportado pelo servidor"
        break
    else:
        print "Resposta do servidor:", resposta