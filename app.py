# Módulo: app.py
# Descrição: Implementa a interface gráfica principal da Gestão de Peças.
# Autor: Glauco Adenauer
# Data de Criação: 14 de Novembro de 2025
# Versão: 1.0

import customtkinter as ctk 
from loginSenha import login # Importa a função de login
import funcoes # Importa as funções de negócio
import time # Importado para uso nas funções

class MainApp(ctk.CTk):
    """
    Classe principal do aplicativo CTkinter para gerenciar a transição
    da tela de Login para a tela do Sistema Principal.
    """
    def __init__(self):
        super().__init__()
        
        # Configuração aparência
        ctk.set_appearance_mode('dark')
        self.title('Gestão de Peças - Login')
        self.geometry('300x350')
        
        # Variável para rastrear o usuário logado
        self.usuario_logado = None
        
        # Frame contendo a tela atual
        self.current_frame = None 
        
        self.mostrar_tela_login()
    
    # -------------------------------------------------------------
    # 1. TELA DE LOGIN
    # -------------------------------------------------------------
    def mostrar_tela_login(self):
        """Cria e exibe a interface de login."""
        
        # Destrói todos os widgets da janela principal antes de carregar o login
        for widget in self.winfo_children():
            widget.destroy()
        
        self.geometry('300x350') # Redimensiona para o login

        # Criação do Frame para a tela de login
        self.frame_login = ctk.CTkFrame(self)
        
        # CORREÇÃO: Usando grid para ocupar todo o espaço
        self.frame_login.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        
        self.current_frame = self.frame_login # Atualiza o frame atual

        #label
        ctk.CTkLabel(self.frame_login, text='Usuário').pack(pady=5)
        
        #entry
        self.campo_usuario = ctk.CTkEntry(self.frame_login, placeholder_text='Digite seu usuário', width=200)
        self.campo_usuario.pack(pady=5)

        #label
        ctk.CTkLabel(self.frame_login, text='Senha').pack(pady=5)
        
        #entry
        self.campo_senha = ctk.CTkEntry(self.frame_login, placeholder_text='Digite sua senha', show="*", width=200) # show="*" para ocultar senha
        self.campo_senha.pack(pady=5)
        
        # Cria o Label DE ERRO AQUI, usando self.frame_login como master
        self.label_erro_login = ctk.CTkLabel(self.frame_login, text="", text_color="red")
        self.label_erro_login.pack(pady=5)

        #Button
        # O comando chama o método de validação da classe
        botao_login = ctk.CTkButton(self.frame_login, text='Login', command=self.validar_login)
        botao_login.pack(pady=10)

        # Criação das funções da funcionalidade

    def validar_login(self):
        """
        Método chamado pelo botão para iniciar a validação de login.
        Passa os campos de entrada e a própria classe (self) para a função de login.
        """
        # Limpa o erro anterior
        self.label_erro_login.configure(text="")
        
        # Chama a função de login e armazena o resultado (True/False ou String de erro)
        resultado = login(self.campo_usuario, self.campo_senha, self)
        
        if isinstance(resultado, str): # Se retornar uma string, é uma mensagem de erro
            self.label_erro_login.configure(text=resultado)
            
    # -------------------------------------------------------------
    # 2. TELA DO SISTEMA PRINCIPAL (MENU)
    # -------------------------------------------------------------
    def iniciar_sistema_principal(self, usuario=None): 
        """
        Destroi a tela atual e cria a tela principal do sistema (menu).
        """
        # Limpa todos os widgets antes de recriar o menu
        for widget in self.winfo_children():
            widget.destroy()
        
        if usuario:
            self.usuario_logado = usuario
        
        if not self.usuario_logado:
            self.mostrar_tela_login()
            return
            
        # Atualiza o título e tamanho da janela
        self.title(f'Gestão de Peças - Bem-vindo, {self.usuario_logado}')
        self.geometry('700x500') 
        
        # Frame principal do menu
        self.frame_principal = ctk.CTkFrame(self)
        # Usando grid para ocupar todo o espaço
        self.frame_principal.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        
        self.current_frame = self.frame_principal # Atualiza o frame atual
        
        # CONTEÚDO DO MENU 
        ctk.CTkLabel(self.frame_principal, text="Menu Principal", font=("Roboto", 24)).pack(pady=25) # Aumentado pady inicial
        
        # Criação dos botões para as funções do menu (agora chamam métodos de tela)
        self.criar_botao_menu("Cadastrar Nova Peça", self.mostrar_tela_cadastro)
        self.criar_botao_menu("Peças Cadastradas (Novas)", self.mostrar_tela_exibir)
        self.criar_botao_menu("Remover Peça Cadastrada", self.mostrar_tela_remover)
        self.criar_botao_menu("Processar Peças (Qualidade)", self.mostrar_tela_processar)
        self.criar_botao_menu("Detalhes de Reprovadas", lambda: self.mostrar_tela_relatorio("Reprovadas")) 
        self.criar_botao_menu("Caixas Fechadas", lambda: self.mostrar_tela_relatorio("Caixas"))
        self.criar_botao_menu("Relatório Geral Consolidado", lambda: self.mostrar_tela_relatorio("Geral"))
        
        ctk.CTkButton(self.frame_principal, text="Sair", command=self.quit, fg_color="red").pack(pady=10, padx=20)
        
    def criar_botao_menu(self, texto, comando):
        """Cria e empacota um botão padrão do menu."""
        # Aplicado pady maior e fill='x' para melhor expansão e espaçamento
        ctk.CTkButton(self.frame_principal, text=texto, command=comando, width=300).pack(pady=8, padx=20, fill='x')

    # -------------------------------------------------------------
    # 3. MÉTODOS DE NAVEGAÇÃO
    # -------------------------------------------------------------
    def mostrar_frame(self, titulo, tamanho, widgets_callback):
        """Método utilitário para criar e exibir um novo frame de tela."""
        # Limpa todos os widgets existentes (incluindo o menu)
        for widget in self.winfo_children():
            widget.destroy()
        
        self.title(f'Gestão de Peças - {titulo}')
        self.geometry(tamanho)
        
        # Usando ScrollableFrame (com grid) para a tela de conteúdo
        novo_frame = ctk.CTkScrollableFrame(self) 
        # Usando grid para ocupar todo o espaço
        novo_frame.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        
        self.current_frame = novo_frame
        
        ctk.CTkLabel(novo_frame, text=titulo, font=("Roboto", 20)).pack(pady=10)
        
        # Adiciona o conteúdo específico da tela (função de callback)
        widgets_callback(novo_frame) 
        
        # Botão Voltar ao Menu
        ctk.CTkButton(self.current_frame, text="Voltar ao Menu", command=self.iniciar_sistema_principal).pack(pady=20)

    # -------------------------------------------------------------
    # 4. TELAS DO MENU (Implementação completa para cada tela)
    # -------------------------------------------------------------
    def mostrar_tela_cadastro(self):
        def criar_widgets(frame):
            # Adaptação da função funcoes.adicionar_pecas para GUI
            
            ctk.CTkLabel(frame, text="Informe os dados da nova peça:", font=("Roboto", 14)).pack(pady=10)
            
            # Campos de entrada
            entry_id_input = self._criar_campo_entry(frame, "ID Numérico da Peça:") # Campo para o input numérico do ID
            entry_cor = self._criar_campo_entry(frame, "Cor:")
            entry_comp = self._criar_campo_entry(frame, "Comprimento (cm):")
            entry_peso = self._criar_campo_entry(frame, "Peso (g):")

            status_label = ctk.CTkLabel(frame, text="", text_color="yellow")
            status_label.pack(pady=10)
            
            def cadastrar_peca_gui():
                try:
                    # Captura de dados da GUI
                    id_input = entry_id_input.get().strip() # Captura o valor e remove espaços
                    cor = entry_cor.get()
                    comp = entry_comp.get()
                    peso = entry_peso.get()

                    # --- LÓGICA DE VALIDAÇÃO E CONCATENAÇÃO DO ID (Início da Mudança) ---
                    if not id_input.isdigit() or not id_input:
                        # Levanta um erro se não for número ou estiver vazio
                        raise ValueError("O ID da peça deve ser um número inteiro e não pode ser vazio.")
                    
                    # Converte o ID para inteiro e formata com zeros à esquerda (ex: 1 -> 01)
                    id_numerico_formatado = f"{int(id_input):02d}" 
                    
                    # Concatenação final: Apontador- + 01
                    id_peca_final = f"Apontador-{id_numerico_formatado}"
                    # -----------------------------------
                    
                    # Validação de outros campos numéricos
                    comp_num = float(comp.replace(',', '.'))
                    peso_num = float(peso.replace(',', '.'))
                    dataPeca = time.strftime("%d/%m/%Y")
                    
                    novo_cadastro = {
                        # Usa o ID formatado e concatenado
                        "ID_Peça": id_peca_final, 
                        "Cor": cor, 
                        "Comprimento": comp_num, 
                        "Peso": peso_num, 
                        "Data_Fabricação": dataPeca, 
                        "Status": "Novo"
                    }
                    
                    funcoes.CADASTRAR_PECAS.append(novo_cadastro)
                    status_label.configure(text=f"Peça {id_peca_final} adicionada com sucesso!", text_color="green")
                    
                    # Limpa os campos
                    entry_id_input.delete(0, 'end'); entry_cor.delete(0, 'end')
                    entry_comp.delete(0, 'end'); entry_peso.delete(0, 'end')

                except ValueError as ve: # Captura o erro específico de validação
                    status_label.configure(text=f"ERRO: {ve}", text_color="red")
                except Exception as e:
                    status_label.configure(text=f"Erro desconhecido: {e}", text_color="red")

            ctk.CTkButton(frame, text="Cadastrar Peça", command=cadastrar_peca_gui).pack(pady=15)
            
        self.mostrar_frame("Cadastrar Nova Peça", '450x600', criar_widgets)
    
    def mostrar_tela_exibir(self):
        def criar_widgets(frame):
            # Adaptação da função funcoes.exibir_pecas para GUI
            
            # Texto/Título do relatório
            ctk.CTkLabel(frame, text="Peças Cadastradas (Status: Novo):", font=("Roboto", 14)).pack(pady=10)
            
            # Cria um Textbox para exibir o conteúdo
            text_box = ctk.CTkTextbox(frame, width=650, height=350, wrap="word")
            text_box.pack(pady=10)
            
            pecas_text = []
            if funcoes.CADASTRAR_PECAS:
                for peca in funcoes.CADASTRAR_PECAS:
                    pecas_text.append(
                        f"ID: {peca['ID_Peça']}, Cor: {peca['Cor']}, Comprim: {peca['Comprimento']}cm, Peso: {peca['Peso']}g, Status: {peca['Status']}"
                    )
                text_box.insert("end", "\n".join(pecas_text))
            else:
                text_box.insert("end", "Nenhuma peça cadastrada aguardando processamento.")
                
            text_box.configure(state="disabled") # Tornar o campo somente leitura

        self.mostrar_frame("Peças Cadastradas (Novas)", '700x550', criar_widgets)
        
    def mostrar_tela_remover(self):
        def criar_widgets(frame):
            # Adaptação da função funcoes.remover_pecas para GUI
            
            ctk.CTkLabel(frame, text="Remover Peça Cadastrada (por Índice):", font=("Roboto", 14)).pack(pady=10)
            
            # 1. Exibição das peças numeradas
            pecas_numeradas = [
                f"[{i}] --> Peça: {p['ID_Peça']}, Status: {p['Status']}" 
                for i, p in enumerate(funcoes.CADASTRAR_PECAS)
            ]
            
            list_box = ctk.CTkTextbox(frame, width=400, height=150)
            if pecas_numeradas:
                list_box.insert("end", "\n".join(pecas_numeradas))
            else:
                list_box.insert("end", "Nenhuma peça cadastrada para remoção.")
                
            list_box.configure(state="disabled")
            list_box.pack(pady=10)

            # 2. Campo para digitar o índice
            entry_indice = self._criar_campo_entry(frame, "Digite o NÚMERO da peça a ser excluída:")
            
            status_label = ctk.CTkLabel(frame, text="", text_color="yellow")
            status_label.pack(pady=10)
            
            def remover_peca_gui():
                try:
                    indice_str = entry_indice.get()
                    indice = int(indice_str)
                    entry_indice.delete(0, 'end')

                    if 0 <= indice < len(funcoes.CADASTRAR_PECAS):
                        peca_removida = funcoes.CADASTRAR_PECAS.pop(indice)
                        status_label.configure(text=f"Peça '{peca_removida['ID_Peça']}' removida com sucesso!", text_color="green")
                        # Recarrega esta tela para atualizar a lista
                        self.mostrar_tela_remover()
                    else:
                        status_label.configure(text="ERRO: Número de peça inválido.", text_color="red")
                        
                except ValueError:
                    status_label.configure(text="ERRO: Entrada inválida. Digite um número inteiro.", text_color="red")
                except Exception as e:
                    status_label.configure(text=f"Erro: {e}", text_color="red")

            ctk.CTkButton(frame, text="Remover Peça", command=remover_peca_gui, fg_color="darkred").pack(pady=10)

        self.mostrar_frame("Remover Peça Cadastrada", '500x550', criar_widgets)
        
    def mostrar_tela_processar(self):
        def criar_widgets(frame):
            # Adaptação da função funcoes.processar_pecas para GUI
            
            ctk.CTkLabel(frame, text="Processamento de Qualidade:", font=("Roboto", 14)).pack(pady=10)
            
            status_label = ctk.CTkLabel(frame, text="Pronto para processar peças novas.", text_color="yellow")
            status_label.pack(pady=10)
            
            def processar_pecas_gui():
                # A função funcoes.processar_pecas faz a lógica e o print no console
                funcoes.processar_pecas() 
                
                # Verificamos as listas globais para dar feedback na GUI
                num_aprovadas = len(funcoes.CAIXAS_FECHADAS) * funcoes.CAPACIDADE_MAX_CAIXA + len(funcoes.CAIXA_ATUAL)
                num_reprovadas = len(funcoes.PECAS_REPROVADAS)
                
                status_label.configure(text=f"Processamento concluído. Aprovadas: {num_aprovadas} | Reprovadas: {num_reprovadas}", text_color="green")
                
            ctk.CTkButton(frame, text="Executar Processamento de Peças", command=processar_pecas_gui).pack(pady=15)
            
        self.mostrar_frame("Processar Peças", '400x300', criar_widgets)

    def mostrar_tela_relatorio(self, tipo):
        def criar_widgets(frame):
            # Adaptação das funções de relatório para GUI
            
            text_box = ctk.CTkTextbox(frame, width=700, height=450, wrap="word")
            text_box.pack(pady=10)
            
            def gerar_relatorio():
                text_box.configure(state="normal")
                text_box.delete("1.0", "end")
                
                if tipo == "Geral":
                    # Funções de Relatório Geral (consolidação)
                    total_aprovadas = len(funcoes.CAIXAS_FECHADAS) * funcoes.CAPACIDADE_MAX_CAIXA + len(funcoes.CAIXA_ATUAL)
                    total_reprovadas = len(funcoes.PECAS_REPROVADAS)
                    
                    text = [
                        "--- RELATÓRIO GERAL CONSOLIDADO ---",
                        f"Total de Peças Aprovadas: {total_aprovadas}",
                        f"Total de Peças Reprovadas: {total_reprovadas}",
                        f"Quantidade de Caixas Fechadas: {len(funcoes.CAIXAS_FECHADAS)}",
                        f"Caixa Atual em Uso: {'Sim' if funcoes.CAIXA_ATUAL else 'Não'} ({len(funcoes.CAIXA_ATUAL)}/{funcoes.CAPACIDADE_MAX_CAIXA} peças)",
                        "\n--- Detalhes das Reprovadas ---"
                    ]
                    if funcoes.PECAS_REPROVADAS:
                        for peca in funcoes.PECAS_REPROVADAS:
                            text.append(f"ID: {peca['ID_Peça']} | Motivo: {peca['Motivo_Reprovacao']}")
                    else:
                        text.append("Nenhuma peça reprovada.")
                    
                    text_box.insert("end", "\n".join(text))

                elif tipo == "Reprovadas":
                    # Detalhes das Reprovadas
                    text = ["--- DETALHES DAS PEÇAS REPROVADAS ---"]
                    if funcoes.PECAS_REPROVADAS:
                        for peca in funcoes.PECAS_REPROVADAS:
                            text.append(f"ID: {peca['ID_Peça']} | Comprim: {peca['Comprimento']} | Peso: {peca['Peso']}g | Cor: {peca['Cor']} | Motivo: {peca.get('Motivo_Reprovacao', 'N/A')}")
                    else:
                        text.append("Nenhuma peça reprovada até o momento.")
                    text_box.insert("end", "\n".join(text))

                elif tipo == "Caixas":
                    # Detalhes das Caixas Fechadas
                    text = ["--- CAIXAS FECHADAS ---"]
                    if funcoes.CAIXAS_FECHADAS:
                        for caixa in funcoes.CAIXAS_FECHADAS:
                            text.append(f"ID: {caixa['ID_Caixa']}, Peças: {len(caixa['Pecas'])}, Data: {caixa['Data_Fechamento']}")
                    else:
                        text.append("Nenhuma caixa fechada ainda.")
                    text_box.insert("end", "\n".join(text))
                        
                text_box.configure(state="disabled")

            #ctk.CTkButton(frame, text=f"Gerar {tipo} Relatório", command=gerar_relatorio).pack(pady=15) * Melhoria imprimir
            gerar_relatorio() # Gera o relatório automaticamente ao abrir a tela
            
        titulo = {"Reprovadas": "Relatório de Reprovadas", "Caixas": "Caixas Fechadas", "Geral": "Relatório Geral Consolidado"}
        self.mostrar_frame(titulo.get(tipo, "Relatório"), '750x650', criar_widgets)

    # -------------------------------------------------------------
    # 5. MÉTODOS AUXILIARES
    # -------------------------------------------------------------
    def _criar_campo_entry(self, master, label_text):
        """Cria um label e um campo de entrada (Entry) agrupados."""
        ctk.CTkLabel(master, text=label_text).pack(pady=(10, 0))
        entry = ctk.CTkEntry(master, width=250)
        entry.pack(pady=(0, 5))
        return entry
        
# Função auxiliar para iniciar a aplicação (para ser chamada em main.py)
def app():
    # Iniciar a aplicação
    main_app = MainApp()
    main_app.mainloop()