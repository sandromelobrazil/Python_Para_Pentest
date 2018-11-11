# -*- coding: utf-8 -*-

print "O texto será ecoado na tela"

# O INPUT() é usado somente para entrada de números
numero = input("Digite um numero: ")

# O RAW_INPUT() é usado somente para entrada de strings
# Caso seja digitado um numero, o mesmo será do tipo string
texto = raw_input("Digite um texto: ")

print type(numero)
print type(texto)