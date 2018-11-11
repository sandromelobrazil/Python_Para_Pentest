nome_completo = "Daniel Moreno" #1

nome_completo_aspas = """Daniel
Henrique
Negri
Moreno""" #2

nome_completo_quebra = "Daniel \
Moreno" #3

nome = "Daniel"
sobrenome = "Moreno"

print "Nome completo (1a forma):", nome_completo #4
print "Nome completo (2a forma):" + nome_completo #5
print "Nome completo (3a forma):" + "Daniel" + "Henrique " + "Negri" + "Moreno" #6
print "Nome completo (4a forma):" + "Daniel" , "Henrique " + "Negri" , "Moreno" #7
print "Nome completo (5a forma):", nome_completo_aspas
print "Nome completo (6a forma):", nome_completo_quebra
print "Nome completo (7a forma): %s" %nome_completo #8
print "Nome completo (8a forma): %s %s" %(nome, sobrenome) #9
print "Nome repetido duas vezes:", nome_completo * 2 #10