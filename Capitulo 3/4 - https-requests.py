import requests

resposta = requests.head("https://site.com")
for cabecalho,conteudo in resposta.headers.iteritems():
    print cabecalho, ":", conteudo