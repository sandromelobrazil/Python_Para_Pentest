import pexpect.pxssh

class Vitima:
    def __init__(self, IP, usuario, senha):
        self.conexao = pexpect.pxssh.pxssh()
        self.conexao.login(IP, usuario, senha)

    def comando(self,comando):
        self.conexao.sendline(comando) #1
        self.conexao.prompt() #2
        print self.conexao.before #3

vitima1 = Vitima("IP_da_vitima", "usuario_SSH", "senha_SSH")