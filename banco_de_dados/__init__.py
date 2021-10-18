from hashlib import sha256 #Importando funções para encriptografar
import mysql.connector

#Class dedicada a trabalhar com o banco de dados

class BancoDados():
    def __init__(self):
        self.login = ''
        self.senha = ''

        self._db = None
        self._cursor = None

    
    def encode_dado(self, txt: str) -> str: #Encripta e retorna a str
        return sha256(txt.encode()).hexdigest()


    def pegar_dados(self):
        self.login = self.encode_dado(input('Login: '))
        self.senha = self.encode_dado(input('Senha: '))

    
    def consultar_dados(self): #Verifica login e senha do adm
        self._cursor.execute("select * from usuarios")
        dados = self._cursor.fetchall()
        
        for user in dados:
            if user[1] == self.login and user[2] == self.senha:
                return True, user

        return False, None


    def insert_dados(self): #Adiciona um novo usuario no banco
        userName = self.encode_dado(input('Login: '))
        password = self.encode_dado(input('Passworld: '))
        autorizacao = input('Tem autorização adm: ').lower().replace('sim','true').replace('não','false')

        command = "INSERT INTO usuarios (nome, senha, ADM) VALUES ('%s','%s','%s')" % (userName,password,autorizacao)

        self._cursor.execute(command)
        self._db.commit()


    def start(self) -> bool:
        try:
            self._db = mysql.connector.connect(host="localhost", user="root", passwd="", database="aps")
            self._cursor = self._db.cursor()
            return True

        except mysql.connector.Error:
            return False