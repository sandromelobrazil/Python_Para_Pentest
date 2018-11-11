import os, base64

arquivo1 = raw_input('Primeiro arquivo: ') #1
arquivo2 = raw_input('Segundo arquivo: ') 

nomeArquivo1 = os.path.basename(arquivo1) #2
nomeArquivo2 = os.path.basename(arquivo2)

with open(arquivo1, 'rb') as arquivo1Aberto: #3
    with open(arquivo2, 'rb') as arquivo2Aberto:
        with open('arquivoFinal.py', 'w') as arquivo_gerado: #4
            arquivo_gerado.write('''import os, base64 #5
def join(conteudoBinario,nomeArquivo): #6
    if not os.path.exists(os.environ["TEMP"] + "\\\\" + nomeArquivo): #7
        with open(os.environ["TEMP"]+ "\\\\" + nomeArquivo, "wb") as arquivoTemporario: #8
            arquivoTemporario.write(conteudoBinario) #9
    os.startfile(os.environ["TEMP"]+ "\\\\" + nomeArquivo) #10
arquivo1base64 = "%s" #11
join(base64.b64decode(arquivo1base64), "%s") #12
arquivo2base64 = "%s" #13
join(base64.b64decode(arquivo2base64), "%s") #14
''' %(base64.b64encode(arquivo1Aberto.read()), nomeArquivo1, \
      base64.b64encode(arquivo2Aberto.read()), nomeArquivo2)) #15