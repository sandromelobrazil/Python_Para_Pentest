import crypt

senha_shadow = raw_input("Digite o hash a ser quebrado:\n")
info = senha_shadow.split(":") #1
usuario = info[0] #2
hash = info[1] #3
salt = hash[:hash.find("$",3)+1] #4

with open("lista.txt", "r") as lista:
    while True:
        senha = lista.readline().strip("\n")
        if not senha:
            break
        if crypt.crypt(senha, salt) == hash: #5
            print "USER \t", usuario
            print "PASS \t", senha
            break