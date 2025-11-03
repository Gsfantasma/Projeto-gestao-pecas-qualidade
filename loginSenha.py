#Login e senha de usuario

import time # Necessário para a função de pausa (sleep)
import sys  # Necessário para a função de saída (exit)

# Variáveis de cadastro
USER_CAD = 'Glauco'
SENHA_CAD = '123'
MAX_TENTATIVAS = 3
TEMPO_BLOQUEIO_SEG = 30

def login():
    # Inicializa a contagem de tentativas (começa em 0 ou 1, aqui usaremos 0 erros)
    tentativa = 0

    print("--- Sistema de Login ---")

    # Loop principal, continuará até que um break ou exit() seja executado
    while True:
        # Pede credenciais
        user = input('Informe o usuario: ')
        senha = input('Informe a senha: ')

        # 1. Verifica se as credenciais estão corretas
        if user == USER_CAD and senha == SENHA_CAD:
            print(f'\n🎉 Bem vindo ao sistema {user}!')
            break #Credenciais corretas: sai do loop e da função
        
        # 2. Se as credenciais estiverem incorretas
        else:
            tentativa += 1 # Incrementa o contador de erros
            
            # Verifica se o limite de tentativas foi atingido
            if tentativa >= MAX_TENTATIVAS:
                print(f'\n🚨 **ERRO!** Limite de {MAX_TENTATIVAS} tentativas excedido.')
                print(f'Usuário bloqueado por {TEMPO_BLOQUEIO_SEG} segundos.')
                
                # Implementa a pausa de 30 segundos
                time.sleep(TEMPO_BLOQUEIO_SEG) 
                
                print('\nTempo de bloqueio finalizado. Tente novamente.')
                # Recomeçar o processo de login
                tentativa = 0 # Reinicia a contagem de tentativas após o bloqueio
            
            # Se não atingiu o limite, repete o loop
            else:
                restantes = MAX_TENTATIVAS - tentativa
                print(f'❌ Usuário ou senha incorreta. Você tem mais {restantes} tentativa(s).')
                print('-' * 20)

# Chama a função
if __name__ == "__main__":
    login()