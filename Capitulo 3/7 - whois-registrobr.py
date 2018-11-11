from bs4 import BeautifulSoup
import requests

IP = "200.200.200.201"

data = {"qr":IP, "captcha-selected":0} #1
resposta = requests.post("https://registro.br/2/whois", data=data) #2

bs = BeautifulSoup(resposta.text, "lxml") #3
bloco_CIDR = bs.find("div", id="whois-output-new") #4
print bloco_CIDR.h2.text #5