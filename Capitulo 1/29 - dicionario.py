# -*- coding: utf-8 -*-

dicionario = {"chave1" : "valor1",
              "chave2" : "valor2",
			  666 : ["alface", "tomate", "cenoura"] }

print "Conteúdo da chave CHAVE1:", dicionario["chave1"]
print "Conteúdo da chave 666:", dicionario[666]
print "Para acessar o valor ALFACE:", dicionario[666][0]

print "Alterando o valor da CHAVE1"
dicionario["chave1"] = "novo valor"