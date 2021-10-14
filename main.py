from UI import UI
from banco_de_dados import BancoDados

inicial = UI(['Logar', 'Sair'], "Banco de dados") #Recebe as opções em uma lista
tela_user = UI(['Ver arquivos', 'Criar login', 'voltar'], "Usuario")
banco_de_dados = BancoDados()
connect = banco_de_dados.start()

while True:
    inicial.start()
    event_inicial = inicial.entrada #event = entrada da opção

    if event_inicial == 1: #Logar
        banco_de_dados.pegar_dados()
        res = banco_de_dados.consultar_dados()
        user = res[1]

        if connect:
            while res[0]:
                tela_user.start()
                event_user = tela_user.entrada

                if event_user == 1: #Ver documentos
                    print("Documento super secreto, só pessoas autorizadas podem ver")
                    input()
                elif event_user == 2: #ADD users
                    if user[3]: #Verifica a permissão
                        banco_de_dados.insert_dados()
                    else:
                        inicial.mensagem_color('Acesso negado', inicial.colors['FAIL'])
                elif event_user == 3: #Volta para tela inicial
                    break
            else:
                inicial.mensagem_color('Acesso negado', inicial.colors['FAIL'])
        else:
            inicial.mensagem_color('Falha ao se conectar ao banco de dados', inicial.colors['WARNING'])

    elif event_inicial == 2: #Sair
        break   