from UI import UI
from banco import BancoDados

windowns = UI(['Logar', 'Criar login', 'Sair']) #Recebe as opções em uma lista
banco_de_dados = BancoDados()

while True:
    windowns.start()
    event = windowns.entrada #event = entrada da opção

    if event == 1:
        banco_de_dados.pegar_dados()
    elif event == 2:
        if banco_de_dados.verificar_adm():
            pass
        else:
            windowns.mensagem_color('Acesso negado', windowns.colors['FAIL'])
    elif event == 3:
        break

        