import requests

URL = "http://site.com/esqueci.html"

usuarios = ["usuario1@mail.com", "usuario2@mail.com"]

for usuario in usuarios:
    data = {"username" : usuario} #1
    resposta = requests.post(URL, data=data)
    if "email não encontrado" not in resposta.text: #2
        print "Login encontrado ->", usuario