class Pessoa:
    def __init__(self, nome, sobrenome): #1
        self.nome = nome #2
        self.sobrenome = sobrenome #3
    def imprime_nome_completo(self):
        return self.nome + self.sobrenome

class Generico(Pessoa): #4
    def altera_nome(self): #5
        self.nome = self.sobrenome 

daniel = Pessoa("Daniel", "Moreno") #6

print daniel.nome #7
print daniel.sobrenome #8
print daniel.imprime_nome_completo() #9

bla = Generico("Nome", "Qualquer") #10
bla.altera_nome()

print bla.nome
print bla.sobrenome
print bla.imprime_nome_completo() #11