from Queue import Queue
import threading, requests

site = "http://site.com"
lock = threading.Lock()

def forca_bruta():
    while not q.empty():
        URL = site + "/" + q.get() #1
        resposta = requests.get(URL) #2
        if resposta.status_code == 200: #3
            if resposta.url[-1] == "/": #4
                lock.acquire()
                print "DIRETORIO ->", resposta.url #5
                lock.release()
            else:
                lock.acquire()
                print "\tARQUIVO ->", resposta.url #6
                lock.release()
        q.task_done()

q = Queue()

for i in range(20):
    t = threading.Thread(target=forca_bruta)
    t.daemon = True
    t.start()

with open("lista.txt") as lista:
    while True:
        nome = lista.readline().strip("\n")
        if not nome:
            break
        q.put(nome)

q.join()