# -*- coding: utf-8 -*-
from importada import *

# Não precisa preceder o nome da função com o nome do script seguido de ponto
teste()

# Não precisa preceder o nome da variável com o nome do script seguido de ponto
print texto

# Caso seja criada uma função com o nome TESTE, a funçãoo importada TESTE é sobrescrita.
# Por isso não se recomenda utilizar FROM SCRIPT IMPORT *
def teste():
    print "Função local sobrescreve a função importada"

teste()