import socks, socket, requests
from bs4 import BeautifulSoup

socks.setdefaultproxy(socks.PROXY_TYPE_SOCKS5, "IP_do_proxy", 666, True) #1
socket.socket = socks.socksocket #2

resposta = requests.get("https://whatismyip.com.br") #3

bs = BeautifulSoup(resposta.text, "lxml")
IP = bs.find("td", {"class" : "left"})
print "IP usado ->", IP.text