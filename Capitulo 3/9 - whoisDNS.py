from bs4 import BeautifulSoup
import requests, socket, netaddr

IP = "IP_do_host"
data = {"qr":IP, "captcha-selected":0}
resposta = requests.post("https://registro.br/2/whois", data=data)

bs = BeautifulSoup(resposta.text, "lxml")
bloco_CIDR = bs.find("div", id="whois-output-new").h2.text.split()[1] #1

ips = netaddr.IPNetwork(bloco_CIDR) #2
for ip in ips: #3
    try:
        print socket.gethostbyaddr(str(ip)) #4
    except:
        pass