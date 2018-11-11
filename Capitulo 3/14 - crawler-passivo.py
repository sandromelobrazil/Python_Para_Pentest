from bs4 import BeautifulSoup
import requests

URL = "https://site.com"

resposta = requests.get(URL)
bs = BeautifulSoup(resposta.text, "lxml")
urls = set() #1

for link in bs.find_all('a'): #2
    if link["href"].startswith(URL): #3
        urls.add(link["href"]) #4

urls_ja_escaneadas = [] #5

while True:

    try:
        url = urls.pop() #6

    except KeyError: #7
        break

    else:
        if url not in urls_ja_escaneadas: #8
            print url #9
            urls_ja_escaneadas.append(url) #10
            resposta = requests.get(url) #11
            bs = BeautifulSoup(resposta.text, "lxml") #12
            for link in bs.find_all('a'): #13
                try:
                    if link["href"].startswith(URL): #14
                        urls.add(link["href"]) #15
                except KeyError:
                    pass