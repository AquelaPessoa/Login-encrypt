from UI import UI
from banco import BancoDados

windowns = UI(['Logar', 'Criar login', 'Sair']) #Recebe as opções em uma lista
banco_de_dados = BancoDados()
connect = banco_de_dados.start()

while True:
    windowns.start()
    event = windowns.entrada #event = entrada da opção

    if event == 1:
        if connect:
            banco_de_dados.pegar_dados()
        else:
            windowns.mensagem_color('Falha ao se conectar ao banco de dados', windowns.colors['FAIL'])
    elif event == 2:
        if banco_de_dados.verificar_adm():
            pass
        else:
            windowns.mensagem_color('Acesso negado', windowns.colors['FAIL'])
    elif event == 3:
        break

        