# -*- coding: utf-8 -*-

def imprime():
    print "Função IMPRIME"

def imprime_nome(nome):
    print "A variável NOME recebe como valor o argumento da função IMPRIME_NOME"
    print "O meu nome é:", nome

def soma(a,b):
    print "Funções podem retornar valores. Nesse caso, a soma de a + b"
    return a + b
    print "O bloco após o RETURN nunca é executado"

imprime()                           # Executa a função IMPRIME
imprime_nome("Daniel Moreno")       # Executa a função IMPRIME_NOME
somatorio = soma(1,2)               # A variável SOMATORIO amazenará o valor 3
print somatorio