# -*- coding: utf-8 -*-

x = 0
while True:
    x += 1
    if x == 10:
        break  #Interrompe o laço de repetição
    elif x == 5:
        continue #Continua no próximo ciclo while, não executando o print
    print "Valor de X ->", x

print "Somente quando x = 10 o resto do script será executado"