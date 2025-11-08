# projeto Gestão de Peças com Qualidade e Armazenamento

#Fabrica de Apontadores GS

import os

from colorama import init, Fore

# Lista principal para armazenar as peças. Padronizado para minúsculas com underscore.
cadastrar_pecas = [
    {
        "ID_Peça": "Apontador-01",
        "Cor": "Verde",
        "Comprimento": "15",
        "Peso": "100",
        "Data_Fabricação": "31/10/2025",
        "Status": " "
    }
]

init(autoreset=True)

def limpar_tela():
    """Limpa o console."""
    # Use 'cls' é para Windows e/ou 'clear' é para Linux/Mac
    os.system("cls" if os.name == "nt" else "clear")

def pausar():
    """Pausa a execução até o usuário apertar Enter."""
    input ("\nAperte ENTER para continuar...")


def adicionar_pecas():
    """Adiciona uma nova peça à lista cadastrar_pecas incluindo data, medidas e status."""
    print(f"{Fore.CYAN}--- Adicionar Novo Apontador ---")
    novaPeca = input("Informe o Id_Peça: ")
    cor = input("Informe a Cor: ")
    comp = input("Digite o comprimento: ")
    peso = input("Digite o peso: ")
    dataPeca = input("Informe a data de fabricação: ")
    status = "Novo"

    # Estrutura (Dicionário)
    novo_cadastro = {
        "ID_Peça": novaPeca,
        "Cor": cor,
        "Comprimento": comp,
        "Peso": peso,
        "Data_Fabricação": dataPeca,
        "Status": status
    }
    
    # Adiciona o dicionário à lista
    cadastrar_pecas.append(novo_cadastro)
    print (f"{Fore.MAGENTA}Peça adicionada com sucesso: {novaPeca}!")

def exibir_pecas():
    """Exibe todas as peças cadastradas e detalhes."""
    if not cadastrar_pecas:
        print(f"{Fore.YELLOW}Nenhuma peça cadastrada para exibição.")
        return
        
    print(f"{Fore.GREEN}--- Lista de Peças Cadastradas ---")
    for peca in cadastrar_pecas:
        print (f"{Fore.GREEN}--> Peça: {peca['ID_Peça']}, Cor: {peca['Cor']}, Comprimento: {peca['Comprimento']}cm, Peso: {peca['Peso']}g, Data_Fabricação: {peca['Data_Fabricação']}, Status: {peca['Status']}")

def exibir_pecas_numeradas():
    """Exibe todas as peças numeradas para fins de remoção."""
    if not cadastrar_pecas:
        print(f"{Fore.YELLOW}Nenhuma peça cadastrada para remoção.")
        return False # Retorna False se a lista estiver vazia

    print(f"{Fore.YELLOW}--- Peças para Remoção ---")
    for index, peca in enumerate(cadastrar_pecas):
        # Exibe o índice e os detalhes da peça
        print (f"{Fore.YELLOW} [{index}] --> Peça: {peca['ID_Peça']}, Cor: {peca['Cor']}, Comprimento: {peca['Comprimento']}cm, Peso: {peca['Peso']}g, Data_Fabricação: {peca['Data_Fabricação']}, Status: {peca['Status']}")
        
    return True # Retorna True se a lista foi exibida


def exibir_menu ():
    """Exibe o menu principal."""
    limpar_tela()
    print (f"{Fore.BLUE}##### GESTÃO DE PEÇAS #####")
    print ("1 - Cadastrar Peça")
    print ("2 - Peças Cadastradas")
    print ("3 - Remover Peça")
    #print ("4 - Caixas Fechadas")
    #print ("5 - Relatorio Peças - Aprovadas")
    #print ("6 - Relatorio Peças - Reprovadas")
    #print ("7 - Relatorio Geral")
    print ("0 - Sair")
    print (f"{Fore.BLUE}###########################")

# --- Lógica Principal do Programa ---

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
        # Verifica se há peças para exibir antes de pedir o número
        if exibir_pecas_numeradas():
            try:
                numero_pecas = int(input(f"{Fore.CYAN}Digite o NÚMERO da peça a ser excluída: "))
                
                # Trata o caso de índice fora do intervalo
                if 0 <= numero_pecas < len(cadastrar_pecas):
                    peca_removida = cadastrar_pecas.pop(numero_pecas)
                    print(f"{Fore.RED}Peça '{peca_removida['ID_Peça']}' removida com sucesso!")
                else:
                    print(f"{Fore.RED}ERRO: Número de peça inválido. Tente novamente.")
                    
            # Trata o caso do usuário não digitar um número
            except ValueError:
                print(f"{Fore.RED}ERRO: Entrada inválida. Digite um número inteiro.")
                
        pausar()
        
    elif resposta == "0":
        limpar_tela()
        print (f"{Fore.BLUE}Saindo do sistema. Até logo!")
        
    else:
        print (f"{Fore.RED}Opção inválida, tente novamente!")
        pausar()