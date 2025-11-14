# projeto Gestão de Peças com Qualidade e Armazenamento

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