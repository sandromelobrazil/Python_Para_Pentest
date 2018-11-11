from bs4 import BeautifulSoup
import requests, re

contador = 0
consulta = 'daniel moreno pentest'
num = 10

headers = {'User-Agent':
'Mozilla/5.0 (X11; Linux x86_64; rv:12.0) Gecko/20100101 Firefox/21.0'}

proxies = ['127.0.0.1:3128', '6.6.6.6:666', '200.200.200.200:80'] #1
proxy = proxies[0] #2
proxies_falharam = [] #3
proxies_detectados_pelo_Google = [] #4

fim = False #5

while True:
    parametros = {'q' : consulta, 'start':contador, 'num':num}

    try:
        resposta = requests.get('http://www.google.com.br/search', params=parametros, 
        headers=headers, timeout=10, proxies={"http" : proxy}) #6
    except Exception: #7
        proxies_falharam.append(proxy) #8
        try:
            proxy = proxies[proxies.index(proxy)+1] #9
        except IndexError: #10
            break
        else: #11
            continue

    if "Our systems have detected unusual traffic from your computer network" in resposta.text:
        a = re.search(r"(\d{1,3}\.){3}\d{1,3}", resposta.text) #12
        proxies_detectados_pelo_Google.append(a.group(0)) #13
        try:
            proxy = proxies[proxies.index(proxy)+1]
        except IndexError:
            break
        else:
            continue

    bs = BeautifulSoup(resposta.text, "lxml")
    cites = bs.find_all("cite")
    if len(cites) == 0:
        fim = True #14
        break

    divs = bs.find_all("div", {"class":"g"})
    for div in divs:
        try:
            print div.h3.a.text
            print div.h3.a["href"]
            print div.find("span", {"class":"st"}).text
            print
        except Exception:
            pass
    contador += 10

if proxies_falharam:
    print "Proxies que falharam:", proxies_falharam
if proxies_detectados_pelo_Google:
    print "Proxies detectados pelo Google:", proxies_detectados_pelo_Google
if not fim:
    print "Busca imcompleta. Inicie uma nova busca com contador =", contador