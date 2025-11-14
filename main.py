# projeto Gestão de Peças com Qualidade e Armazenamento
# Módulo: main.py
# Descrição: Implenta a chamada principal
# Autor: Glauco Adenauer
# Data de Criação: 14 de Novembro de 2025
# Versão: 1.0

#Fabrica de Apontadores GS

# main.py
#  Funções são chamadas via app.py
#  Login é chamado via app.py

from app import app # Importa a função app() que inicia a classe MainApp

# --- Lógica Principal do Programa ---

if __name__ == "__main__":
    # Inicia a tela de login
    # Todo o fluxo (login e abertura do menu) é gerenciado pela GUI.
    app() 
    # A execução do console é encerrada após o fechamento da janela
print("Sistema encerrado.")

#Objetivo principal é fazer apenas chamada principal mantendo a segurança do codigo e preservando regras de negocio e dados internos