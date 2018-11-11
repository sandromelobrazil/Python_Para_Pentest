import socket
dominio = "dominio.com"
nomes = ["ns1", "ns2", "www", "ftp", "intranet"]

for nome in nomes:
    DNS = nome + "." + dominio #1
    try:
        print DNS + ": " + socket.gethostbyname(DNS) #2
    except socket.gaierror: #3
        pass