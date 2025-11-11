#Funções de execuçao do programa

# funcoes.py
import os
from colorama import init, Fore
from datetime import datetime

# Inicializa o colorama
init(autoreset=True)

# --- Variáveis de Estado Global ---
# Lista principal. Peças aprovadas serão movidas para 'caixas_fechadas' ou 'caixa_atual'
CADASTRAR_PECAS = [ 
    {
        "ID_Peça": "Apontador-01",
        "Cor": "Verde",
        "Comprimento": 15.0, # Convertido para float/int para validação
        "Peso": 100.0,      # Convertido para float/int para validação
        "Data_Fabricação": "31/10/2025",
        "Status": "Aprovado"
    }
]

# Variáveis de Armazenamento e Relatório
PECAS_REPROVADAS = []
CAIXAS_FECHADAS = []
CAIXA_ATUAL = []
CAPACIDADE_MAX_CAIXA = 3 

# --- Funções Utilitárias ---

def limpar_tela():
    """Limpa o console."""
    os.system("cls" if os.name == "nt" else "clear")

def pausar():
    """Pausa a execução até o usuário apertar Enter."""
    input ("\nAperte ENTER para continuar...")

# --- Funções de Negócio ---

def avaliar_qualidade(peca):
    """
    Avalia a peça com base nos critérios de qualidade e retorna o status
    ('Aprovado' ou 'Reprovado') e o motivo da reprovação.
    """
    motivo = []
    
    try:
        # Conversão de tipos para avaliação de comparações
        peso = float(peca['Peso'])
        comprimento = float(peca['Comprimento'])
        cor = peca['Cor'].lower()
        
        # Critério 1: Peso
        if not (95 <= peso <= 105):
            motivo.append("Peso fora do intervalo (95g-105g)")
            
        # Critério 2: Cor
        if cor not in ["azul", "verde"]:
            motivo.append("Cor inválida (deve ser Azul ou Verde)")
            
        # Critério 3: Comprimento
        if not (10 <= comprimento <= 20):
            motivo.append("Comprimento fora do intervalo (10cm-20cm)")
            
    except ValueError:
        motivo.append("Dados de Peso/Comprimento inválidos (não são números)")
    """Avalia os 3 criterios principais da qualidade antes de adicionar a caixa"""
    if not motivo:
        return "Aprovado", None
    else:
        return "Reprovado", ", ".join(motivo)

def gerenciar_caixas(peca_aprovada):
    """
    Adiciona a peça aprovada à CAIXA_ATUAL. Se a capacidade for atingida (10),
    fecha a caixa e inicia uma nova.
    """
    global CAIXA_ATUAL, CAIXAS_FECHADAS

    CAIXA_ATUAL.append(peca_aprovada)
    print(f"{Fore.MAGENTA}Peça '{peca_aprovada['ID_Peça']}' adicionada à caixa atual ({len(CAIXA_ATUAL)}/{CAPACIDADE_MAX_CAIXA}).")
    
    if len(CAIXA_ATUAL) >= CAPACIDADE_MAX_CAIXA:
        # Cria uma cópia da caixa antes de fechar e adicionar, ou a lista será alterada
        caixa_fechada = {
            "ID_Caixa": f"CX-{len(CAIXAS_FECHADAS) + 1:03d}",
            "Pecas": list(CAIXA_ATUAL),
            "Data_Fechamento": datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        }
        
        CAIXAS_FECHADAS.append(caixa_fechada)
        CAIXA_ATUAL = []  # Inicia uma nova caixa
        print(f"\n{Fore.CYAN}*** CAIXA FECHADA ***")
        print(f"{Fore.CYAN}Caixa '{caixa_fechada['ID_Caixa']}' com {CAPACIDADE_MAX_CAIXA} peças.")
        print(f"{Fore.CYAN}Nova caixa iniciada automaticamente.")


def processar_pecas():
    """
    CADASTRAR_PECAS, avalia cada uma e a classifica como Aprovada/Reprovada.
    As peças são movidas para o armazenamento (caixas) ou para o repositório de reprovadas.
    """
    global CADASTRAR_PECAS, PECAS_REPROVADAS
    
    if not CADASTRAR_PECAS:
        print(f"{Fore.YELLOW}Nenhuma peça nova cadastrada para processamento.")
        return
        
    print(f"{Fore.CYAN}--- Processamento de Qualidade ---")
    
    # Cria novas listas para as peças processadas e reprovadas
    # Usa um índice para percorrer sem remover elementos
    i = 0
    pecas_a_remover = []
    
    while i < len(CADASTRAR_PECAS):
        peca = CADASTRAR_PECAS[i]
        
        # Só processa peças que ainda não tem um status final
        if peca['Status'] in ["Novo", " "]:
            status, motivo = avaliar_qualidade(peca)
            peca['Status'] = status
            
            if status == "Aprovado":
                gerenciar_caixas(peca)
            else:
                peca['Motivo_Reprovacao'] = motivo
                PECAS_REPROVADAS.append(peca)
            
            pecas_a_remover.append(i) # Marca o índice da peça para remoção posterior

        i += 1
        
    # Remove as peças processadas da lista principal
    # É melhor remover de trás para frente para evitar problemas de índice *Ponto de melhoria
    for index in sorted(pecas_a_remover, reverse=True):
        CADASTRAR_PECAS.pop(index)

    print(f"{Fore.MAGENTA}Processamento concluído. {len(pecas_a_remover)} peça(s) avaliada(s).")

# --- Funções de Interface/CRUD ---

def adicionar_pecas():
    """Adiciona uma nova peça à lista CADASTRAR_PECAS (antes da avaliação)."""
    print(f"{Fore.CYAN}--- Adicionar Novo Apontador ---")
    novaPeca = input("Informe o Id_Peça: ")
    cor = input("Informe a Cor: ")
    comp = input("Digite o comprimento (cm): ")
    peso = input("Digite o peso (g): ")
    dataPeca = datetime.now().strftime("%d/%m/%Y") # Usa a data/hora atual
    status = "Novo"

    # Converte os valores para float/int assim que possível para maior confiabilidade
    try:
        comp_num = float(comp.replace(',', '.'))
        peso_num = float(peso.replace(',', '.'))
    except ValueError:
        print(f"{Fore.RED}ERRO: Peso e Comprimento devem ser valores numéricos. Peça não adicionada.")
        return

    # Estrutura (Dicionário)
    novo_cadastro = {
        "ID_Peça": novaPeca,
        "Cor": cor,
        "Comprimento": comp_num,
        "Peso": peso_num,
        "Data_Fabricação": dataPeca,
        "Status": status
    }
    
    CADASTRAR_PECAS.append(novo_cadastro)
    print (f"{Fore.MAGENTA}Peça adicionada com sucesso: {novaPeca}!")

def exibir_pecas():
    """Exibe todas as peças cadastradas (sem status final)."""
    if not CADASTRAR_PECAS:
        print(f"{Fore.YELLOW}Nenhuma peça cadastrada para exibição (aguardando processamento).")
        return
        
    print(f"{Fore.GREEN}--- Lista de Peças Cadastradas (Status: Novo) ---")
    for peca in CADASTRAR_PECAS:
        print (f"{Fore.GREEN}--> Peça: {peca['ID_Peça']}, Cor: {peca['Cor']}, Comprimento: {peca['Comprimento']}cm, Peso: {peca['Peso']}g, Data_Fabricação: {peca['Data_Fabricação']}")

def exibir_pecas_numeradas():
    """Exibe todas as peças numeradas para fins de remoção."""
    if not CADASTRAR_PECAS:
        print(f"{Fore.YELLOW}Nenhuma peça cadastrada para remoção.")
        return False

    print(f"{Fore.YELLOW}--- Peças para Remoção ---")
    for index, peca in enumerate(CADASTRAR_PECAS):
        print (f"{Fore.YELLOW} [{index}] --> Peça: {peca['ID_Peça']}, Status: {peca['Status']}")
        
    return True

def remover_pecas():
    """Função para remover uma peça cadastrada (Novo) pelo índice."""
    if exibir_pecas_numeradas():
        try:
            numero_pecas = int(input(f"{Fore.CYAN}Digite o NÚMERO da peça a ser excluída: "))
            
            if 0 <= numero_pecas < len(CADASTRAR_PECAS):
                peca_removida = CADASTRAR_PECAS.pop(numero_pecas)
                print(f"{Fore.RED}Peça '{peca_removida['ID_Peça']}' removida com sucesso!")
            else:
                print(f"{Fore.RED}ERRO: Número de peça inválido. Tente novamente.")
                
        except ValueError:
            print(f"{Fore.RED}ERRO: Entrada inválida. Digite um número inteiro.")

# --- Funções de Relatórios ---

def relatorio_consolidado():
    """Gera um relatório completo do estado atual do sistema."""
    
    total_aprovadas = len(CAIXAS_FECHADAS) * CAPACIDADE_MAX_CAIXA + len(CAIXA_ATUAL)
    total_reprovadas = len(PECAS_REPROVADAS)
    total_caixas_utilizadas = len(CAIXAS_FECHADAS) + (1 if CAIXA_ATUAL else 0)
    
    print(f"{Fore.GREEN}--- Relatório Geral de Produção ---")
    print(f"{Fore.GREEN}Total de Peças Aprovadas: {total_aprovadas}")
    print(f"{Fore.RED}Total de Peças Reprovadas: {total_reprovadas}")
    print(f"{Fore.CYAN}Quantidade de Caixas Fechadas: {len(CAIXAS_FECHADAS)}")
    print(f"{Fore.CYAN}Caixa Atual em Uso: {'Sim' if CAIXA_ATUAL else 'Não'} ({len(CAIXA_ATUAL)}/{CAPACIDADE_MAX_CAIXA} peças)")
    print(f"{Fore.MAGENTA}Total de Caixas Utilizadas (Fechadas + Aberta): {total_caixas_utilizadas}")
    
    print("\n--- Detalhes das Reprovadas ---")
    if PECAS_REPROVADAS:
        for peca in PECAS_REPROVADAS:
            print(f"{Fore.RED}ID: {peca['ID_Peça']} | Motivo: {peca['Motivo_Reprovacao']}")
    else:
        print(f"{Fore.GREEN}Nenhuma peça reprovada.")

def exibir_caixas_fechadas():
    """Exibe os IDs das caixas fechadas."""
    if not CAIXAS_FECHADAS:
        print(f"{Fore.YELLOW}Nenhuma caixa fechada ainda.")
        return
        
    print(f"{Fore.CYAN}--- Caixas Fechadas ({len(CAIXAS_FECHADAS)}) ---")
    for caixa in CAIXAS_FECHADAS:
        print(f"{Fore.CYAN}ID: {caixa['ID_Caixa']}, Peças: {len(caixa['Pecas'])}, Data: {caixa['Data_Fechamento']}")

def exibir_menu():
    """Exibe o menu principal."""
    limpar_tela()
    print (f"{Fore.BLUE}##### GESTÃO DE PEÇAS #####")
    print ("1 - Cadastrar Nova Peça")
    print ("2 - Peças Cadastradas (Novas)")
    print ("3 - Remover Peça Cadastrada")
    print ("4 - ** Processar Peças (Qualidade e Armazenamento) **")
    print ("---")
    print ("5 - Relatório de Peças Reprovadas")
    print ("6 - Caixas Fechadas")
    print ("7 - Relatório Geral Consolidado")
    print ("0 - Sair")
    print (f"{Fore.BLUE}###########################")