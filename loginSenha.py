# loginSenha.py
import time
import sys

# Variáveis de cadastro
USER_CAD = 'Glauco'
SENHA_CAD = '123'
MAX_TENTATIVAS = 3
TEMPO_BLOQUEIO_SEG = 30

# Variáveis globais para controle de estado do login
tentativas = 0
bloqueio = 0 # time.time() quando o bloqueio termina

def login(usuario_ent, senha_ent, app_handler): # Recebe os campos e o handler da classe
    """
    Executa a validação de login para a interface CTkinter.
    Se bem-sucedido, chama o método para iniciar o sistema principal na classe App.
    Retorna True em sucesso, ou uma string de erro em falha.
    """
    global tentativas, bloqueio

    # Obtém os valores dos campos de entrada
    user = usuario_ent.get()
    senha = senha_ent.get()
            
    # 1. Verifica se está bloqueado
    if time.time() < bloqueio:
        tempo_restante = int(bloqueio - time.time())
        # Retorna a string de erro para a GUI
        return f"Usuário bloqueado.\n Tente novamente em {tempo_restante} segundos."

    # 2. Validação e Ação de Sucesso
    if user == USER_CAD and senha == SENHA_CAD:
        print(f'\n🎉 Bem vindo ao sistema {user}!')
        tentativas = 0 # Reseta em caso de sucesso
        
        # AÇÃO CHAVE: Chama o método da classe MainApp para mudar para a tela principal
        app_handler.iniciar_sistema_principal(user)
        
        # Login bem-sucedido
        return True
    
    else:
        # Lógica de falha
        tentativas += 1
        
        if tentativas >= MAX_TENTATIVAS:
            bloqueio = time.time() + TEMPO_BLOQUEIO_SEG
            
            tentativas = 0 # Reinicia a contagem de tentativas
            # Retorna a string de erro para a GUI
            return f'🚨 ERRO! Limite de {MAX_TENTATIVAS} tentativas excedido.\n Usuário bloqueado por {TEMPO_BLOQUEIO_SEG} segundos.'
        
        else:
            restantes = MAX_TENTATIVAS - tentativas
            # Retorna a string de erro para a GUI
            return f'❌ Usuário ou senha incorreta.\n Você tem mais {restantes} tentativa(s).'