import requests

resposta = requests.head("http://site.com") #1
for cabecalho,conteudo in resposta.headers.iteritems(): #2
    print cabecalho, ":", conteudo