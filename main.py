# projeto Gestão de Peças com Qualidade e Armazenamento

#Fabrica de Apontadores GS

# main.py
from funcoes import *
from loginSenha import login

# --- Lógica Principal do Programa ---

# 1. Realiza o login
if __name__ == "__main__":
    if not login():
        # Se o login falhar (embora login.py não retorne explicitamente False neste design,
        # é uma boa prática para modularidade), encerra a execução. *Ponto de melhoria
        sys.exit() 
    
    pausar() # Pausa após o login bem-sucedido
    
    # 2. Loop principal do menu
    resposta = ""
    while resposta != "0":
        exibir_menu()
        resposta = input ("Escolha uma opção: ")
        
        if resposta == "1":
            limpar_tela()
            adicionar_pecas()
            pausar()
            
        elif resposta == "2":
            limpar_tela()
            exibir_pecas()
            pausar()
            
        elif resposta == "3":
            limpar_tela()
            remover_pecas()
            pausar()
            
        elif resposta == "4":
            limpar_tela()
            processar_pecas()
            pausar()
            
        elif resposta == "5":
            limpar_tela()
            # O relatório de reprovadas é parte do relatório geral, mas foi simplificado
            # Mostra os reprovados da consolidação Geral.
            print(f"{Fore.RED}--- Peças Reprovadas ---")
            if PECAS_REPROVADAS:
                for peca in PECAS_REPROVADAS:
                     print(f"{Fore.RED}ID: {peca['ID_Peça']} | Peso: {peca['Peso']}g | Cor: {peca['Cor']} | Comp: {peca['Comprimento']}cm | Motivo: {peca.get('Motivo_Reprovacao', 'N/A')}")
            else:
                 print(f"{Fore.GREEN}Nenhuma peça reprovada até o momento.")
            pausar()
            
        elif resposta == "6":
            limpar_tela()
            exibir_caixas_fechadas()
            pausar()
            
        elif resposta == "7":
            limpar_tela()
            relatorio_consolidado()
            pausar()
            
        elif resposta == "0":
            limpar_tela()
            print (f"{Fore.BLUE}Saindo do sistema. Até logo!")
            
        else:
            print (f"{Fore.RED}Opção inválida, tente novamente!")
            pausar()