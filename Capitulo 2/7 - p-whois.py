import whois

dominio = "dominio.com"
consultaWhois = whois.whois(dominio)

print consultaWhois.email #1
print consultaWhois["email"] #2
print consultaWhois.text #3