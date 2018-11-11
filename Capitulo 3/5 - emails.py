import requests, re

resposta = requests.get("http://localhost/emails.html")

#Fonte: Effective Python Penetration Testing, pag.58
emails = set(re.findall(r"[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.[a-z]+", resposta.text, re.I)) #1
print emails