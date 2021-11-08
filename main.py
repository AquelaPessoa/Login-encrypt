from UI import UI
from banco_de_dados import BancoDados
import os

inicial = UI(['Logar', 'Sair'], "Site super secreto do governo") #Recebe as opções em uma lista
tela_user = UI(['Ver documentos', 'Criar login', 'voltar'], "Bem vindo")

banco_de_dados = BancoDados()
is_connect = banco_de_dados.connect()

while True:
    inicial.start()
    event_inicial = inicial.entrada #event = entrada da opção

    if is_connect:
        if event_inicial == 1: #Logar
            banco_de_dados.pegar_dados()
            res = banco_de_dados.consultar_dados()
            user = res[1]
            
            while res[0]:
                tela_user.start()
                event_user = tela_user.entrada

                #Criando lista de arquivos
                arquivos = []
                [arquivos.append(arquivo) for _, _, arquivo in os.walk("./documents/")]
                arquivos = arquivos[0]
                
                tela_documentos = UI(arquivos, "Documentos")

                if event_user == 1: #Ver documentos
                    tela_documentos.start()
                    event_document = tela_user.entrada

                    with open(f"./documents/{arquivos[event_document - 1]}", "r", encoding="utf-8") as f:
                        print(f.read())
                        input()

                elif event_user == 2: #ADD users
                    if user[3]: #Verifica a permissão
                        banco_de_dados.insert_dados()
                        inicial.mensagem_color('Usuario criado', inicial.colors['OKGREEN'])
                    else:
                        inicial.mensagem_color('Acesso negado', inicial.colors['FAIL'])
                elif event_user == 3: #Volta para tela inicial
                    break
            else:
                inicial.mensagem_color('Acesso negado', inicial.colors['FAIL'])
    
    else:
        inicial.mensagem_color('Falha ao se conectar ao banco de dados', inicial.colors['WARNING'])
    
    if event_inicial == 2: #Sair
            break