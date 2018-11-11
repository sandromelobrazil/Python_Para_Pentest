from bs4 import BeautifulSoup
import requests

contador = 0 #1
consulta = 'daniel moreno pentest'
num = 10 #2

headers = {'User-Agent':
'Mozilla/5.0 (X11; Linux x86_64; rv:12.0) Gecko/20100101 Firefox/21.0'} #3

while True:
    parametros = {'q' : consulta, 'start':contador, 'num':num} #4
    resposta = requests.get('http://www.google.com.br/search', params=parametros, timeout=2, headers=headers) #5

    if "Our systems have detected unusual traffic from your computer network" in resposta.text: #6
        print "O Google detectou o comportamento da bot. Saindo..."
        break

    bs = BeautifulSoup(resposta.text, "lxml")
    cites = bs.find_all("cite") #7
    if len(cites) == 0: #8
        break

    divs = bs.find_all("div", {"class":"g"}) #9
    for div in divs:
        try:
            print div.h3.a.text #10
            print div.h3.a["href"] #11
            print div.find("span", {"class":"st"}).text #12
            print
        except Exception:
            pass
    contador += 10