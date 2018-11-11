# -*- coding: utf-8 -*-

lista = [1,2,3,4]

try:
    valor = input("Digite 1 ou 2: ")
    if valor == 1:
        print lista[4]
    elif valor == 2:
        1/0
    else:
        print  "Apenas 1 ou 2"
        exit() # Sai do programa
except IndexError:
    print "Exceção do tipo IndexError"
except ZeroDivisionError:
    print "Exceção do tipo ZeroDivisionError"
