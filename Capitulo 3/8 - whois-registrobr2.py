from bs4 import BeautifulSoup
import requests

IP = "200.200.200.201"
data = {"qr":IP, "captcha-selected":0}

resposta = requests.post("https://registro.br/2/whois", data=data)
bs = BeautifulSoup(resposta.text, "lxml")
info = bs.find("div", id="whois-output-plain")
print info.text