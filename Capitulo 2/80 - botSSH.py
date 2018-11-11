import paramiko

class Vitima: #1
    def __init__(self, IP, usuario, senha): #2
        self.conexao = paramiko.SSHClient() #3
        self.conexao.set_missing_host_key_policy(paramiko.AutoAddPolicy()) #4
        self.conexao.connect(IP, username=usuario, password=senha) #5
        self.sftp = self.conexao.open_sftp() #6

    def comando(self,comando): #7
        stdin, stdout, stderr = self.conexao.exec_command(comando) #8
        for resultado in stdout.readlines() + stderr.readlines():
            print resultado.strip()

    def download(self,remoto,local): #9
        self.sftp.get(remoto,local)

    def upload(self,local,remoto): #10
        self.sftp.put(local, remoto)

    def chdir(self,dir): #11
        self.sftp.chdir(dir)

    def getcwd(self): #12
        print self.sftp.getcwd()

    def listdir(self): #13
        for arquivos in self.sftp.listdir():
            print arquivos

    def fechar(self): #14
        self.conexao.close()

vitima1 = Vitima("IP_da_vitima", "usuario_SSH", "senha_SSH") #15