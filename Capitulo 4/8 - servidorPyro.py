import Pyro4, threading
from parse import *

@Pyro4.expose
class Dist: #1
    def quebra(self): #2
        return lista.pop()

    def achou(self, quebrou): #3
        global senha
        senha = quebrou

    def verifica_se_achou_a_senha(self): #4
        global senha
        return senha

    def incrementa_listaAuxiliar(self, palavra): #5
        listaAuxiliar.add(palavra)

    def pega_info(self): #6
        global ssid, aNonce, sNonce, apMac, cliMac, \
               frame802_1, frame802_2, frame802_3, mic1, mic2, mic3
        return (ssid, aNonce, sNonce, apMac, cliMac, \
               frame802_1, frame802_2, frame802_3, mic1, mic2, mic3)

def iniciaPyro(): #7
    daemon = Pyro4.Daemon(host="192.168.0.3", port=666)
    uri = daemon.register(Dist(), "dist")
    print uri #8
    daemon.requestLoop()

def menu(): #9
    print "\n(p)rogresso"
    print "(s)enha descoberta?"

lista = set(["senha", "senha123", "admin"]) #10
listaBackup = lista.copy() #11
listaAuxiliar = set() #12
senha = "" #13

threading.Thread(target=iniciaPyro).start()

while True:
    menu()
    opcao = raw_input("\nEscolha uma opcao: ")

    if opcao == "p":
        progresso = len(listaBackup.difference(listaAuxiliar))
        print "\n\t\tFaltam %d palavras a serem processadas" %progresso #14

    elif opcao == "s":
        print "\n\t\tSenha descoberta ->", senha