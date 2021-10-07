from hashlib import sha256 #Importando funções para encriptografar

#Class dedicada a trabalhar com o banco de dados

class BancoDados():
    def __init__(self):
        self.login = ''
        self.senha = ''

        self._admin_login = '8c6976e5b5410415bde908bd4dee15dfb167a9c873fc4bb8a81f6f2ab448a918'
        self._admin_senha = '8c6976e5b5410415bde908bd4dee15dfb167a9c873fc4bb8a81f6f2ab448a918' 

    #Encripta e retorna a str
    def encode_dado(self, txt: str) -> str:
        return sha256(txt.encode()).hexdigest()


    def pegar_dados(self):
        self.login = self.encode_dado(input('Login: '))
        self.senha = self.encode_dado(input('Senha: '))

    #Verifica login e senha do adm (pode mudar)
    def verificar_adm(self) -> bool:
        if self._admin_login == self.encode_dado(input("Adm login: ")) and self._admin_senha == self.encode_dado(input("Adm senha: ")):
            return True
        else:
            return False


    def salvar_dados(self):
        pass