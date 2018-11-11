# -*- coding: utf-8 -*-
import smtplib

conexao_SMTP = smtplib.SMTP('site.com', 25)
conexao_SMTP.ehlo()

FROM = "falso@email.com"
TO = "destinatario@site.com"
SUBJECT = "Cabeçalho da mensagem"
BODY = "Aqui entra o corpo do email falso"

mensagem = """From: %s
To: %s
Subject: %s

%s""" % (FROM, TO, SUBJECT, BODY)

conexao_SMTP.sendmail(FROM, TO, mensagem)