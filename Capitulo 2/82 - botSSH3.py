import pexpect
SHELL = ['# ', '$ ']

class Vitima:
    def __init__(self, IP, usuario, senha):
        self.conexao = pexpect.spawn('ssh %s@%s' %(usuario,IP)) #1
        ret = self.conexao.expect(['Are you sure you want to', 'password:']) #2
        if ret == 0: #3
            self.conexao.sendline("yes") #4
            self.conexao.expect('password:') #5
        self.conexao.sendline(senha) #6
        self.conexao.expect(SHELL) #7

    def comando(self,comando):
        self.conexao.sendline(comando)
        self.conexao.expect(SHELL)
        print self.conexao.before

vitima1 = Vitima("IP_da_vitima", "usuario_SSH", "senha_SSH")