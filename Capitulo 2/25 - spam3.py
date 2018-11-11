# -*- coding: utf-8 -*-
import requests

FROM = "falso@email.com"
TO = "destinatario@site.com"
SUBJECT = "Cabeçalho da mensagem"
BODY = "Aqui entra o corpo do email falso"

data = {"FROM" : FROM,
        "TO" : TO,
        "SUBJECT" : SUBJECT,
        "BODY": BODY
}

requests.post("http://site.com/spam3.php", data = data)
print "Email falso enviado com sucesso"