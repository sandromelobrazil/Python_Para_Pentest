with open("arquivo.exe", "rb") as arquivo:
    conteudo = arquivo.read()

with open("COPIA_arquivo.exe", "wb") as arquivo:
    arquivo.write(conteudo)