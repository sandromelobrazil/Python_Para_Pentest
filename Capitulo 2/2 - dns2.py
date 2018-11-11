import socket

dominio = "dominio.com"

with open("brute-force.txt") as arquivo: #1
    nomes = arquivo.readlines() #2

for nome in nomes:
    DNS = nome.strip("\n") + "." + dominio #3
    try:
        print DNS + ": " + socket.gethostbyname(DNS)
    except socket.gaierror:
        pass