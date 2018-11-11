import requests

host = "http://site.com"
metodos = ['OPTIONS', 'GET', 'POST', 'PUT', 'DELETE', 'TRACE', 'CONNECT', 'QUALQUER']

for metodo in metodos:
    resposta = requests.request(metodo, host)
    print metodo, "->", resposta.reason