#Login e senha de usuario

# loginSenha.py
import time
import sys

# Variáveis de cadastro
USER_CAD = 'Glauco'
SENHA_CAD = '123'
MAX_TENTATIVAS = 3
TEMPO_BLOQUEIO_SEG = 30

def login():
    """
    Controla o processo de login, verificando credenciais e
    implementando o limite de tentativas com bloqueio temporário.
    Retorna True se o login for bem-sucedido, False caso contrário (e encerra o programa).
    """
    tentativa = 0

    print("--- Sistema de Login ---")

    while True:
        user = input('Informe o usuario: ')
        senha = input('Informe a senha: ')

        if user == USER_CAD and senha == SENHA_CAD:
            print(f'\n🎉 Bem vindo ao sistema {user}!')
            return True  # Login bem-sucedido
        
        else:
            tentativa += 1
            
            if tentativa >= MAX_TENTATIVAS:
                print(f'\n🚨 **ERRO!** Limite de {MAX_TENTATIVAS} tentativas excedido.')
                print(f'Usuário bloqueado por {TEMPO_BLOQUEIO_SEG} segundos.')
                time.sleep(TEMPO_BLOQUEIO_SEG)
                
                print('\nTempo de bloqueio finalizado. Tente novamente.')
                tentativa = 0 # Reinicia a contagem de tentativas
            
            else:
                restantes = MAX_TENTATIVAS - tentativa
                print(f'❌ Usuário ou senha incorreta. Você tem mais {restantes} tentativa(s).')
                print('-' * 20)