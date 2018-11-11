import pexpect.pxssh

host = "localhost"
usuario = "root"
senhas = ["root", "toor"]

for senha in senhas:
    try:
        ps = pexpect.pxssh.pxssh()
        ps.login(host,usuario,senha)
    except:
        pass
    else:
        print "USER:", usuario
        print "PASS:", senha
    finally:
        ps.close()