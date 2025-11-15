README
Markdown
# ⚙️ Desafio de Automação Digital: Gestão de Peças, Qualidade e Armazenamento

## 🎯 Explicação do Funcionamento

Este projeto é um protótipo de sistema de automação para controle de qualidade e gestão de estoque em uma linha de montagem de apontadores. Utiliza uma **Interface Gráfica de Usuário (GUI)** construída com a biblioteca `customtkinter`.

**Lógica de Qualidade**: As peças são avaliadas com base em critérios estritos (Peso, Cor, Comprimento). Peças aprovadas são armazenadas em caixas (capacidade de 10 peças/caixa no protótipo) e peças reprovadas são registradas com o motivo da falha.

[Link Youtube](https://www.youtube.com/watch?v=6_LJbLGR7pY).

## 🚀 Como Rodar o Programa (Passo a Passo)

### Pré-requisitos

O projeto requer a instalação das bibliotecas `customtkinter` e `colorama`.

1.  **Instalar Python:** Certifique-se de ter o Python 3.7 ou superior instalado.
2.  **Instalar Bibliotecas:** Abra o terminal e execute os seguintes comandos:

    ```bash
    pip install customtkinter
    pip install colorama
    ```
    * Para mais informações sobre a instalação de pacotes Python, consulte a documentação oficial da plataforma Python:
 [Guia de Instalação do Python](https://docs.python.org/pt-br/3/installing/index.html).

### Execução

1.**Baixar o Código:** Clone o repositório GitHub ( https://github.com/Gsfantasma/Projeto-gestao-pecas-qualidade) ou baixe os arquivos.
2.  **Executar o Módulo Principal:** Navegue até o diretório do projeto no terminal e execute o arquivo `main.py`:

    ```bash
    python main.py
    ```
### Login de Acesso

Ao iniciar, o sistema exibirá a tela de Login:

* **Usuário Padrão**: “Glauco”
* **Senha Padrão**: “123”
* **Segurança**: O sistema bloqueia o acesso por 30 segundos após 3 tentativas de login falhas.

## 💻 Exemplos de Entradas e Saídas (Funcionalidades Principais)

### 1. Cadastrar Nova Peça (Tela: Cadastrar Nova Peça)

| Entrada (ID Numérico) | Entrada (Comprimento) | Entrada (Peso) | Entrada (Cor) | Saída Após Processamento |
| :--- | :--- | :--- | :--- | :--- |
| 1 | 15.0 | 100.0 | Verde | Aprovado |
| 2 | 5.0 | 98.0 | Azul | Reprovado (Comprimento fora do intervalo) |
| 3 | 12.0 | 120.0 | Azul | Reprovado (Peso fora do limite) |

### 2. Processar Peças (Tela: Processar Peças)

Esta função move todas as peças com Status: “Novo” para esteira de validação final, acionando a lógica de qualidade e gerenciamento de caixas.

* **Saída Esperada (Aprovadas)**: Se 10 peças forem aprovadas, o sistema fechará a **Caixa CX-001** e iniciará uma nova.
* **Saída Esperada (Reprovadas)**: As peças reprovadas são listadas no **Relatório de Reprovadas** com o `Motivo_Reprovacao`.

### 3. Relatórios (Tela: Relatório Geral Consolidado)
Exibe o balanço geral da produção, essencial para o controle de estoque e qualidade.

* **Informações**: Total de Peças Aprovadas, Total de Peças Reprovadas, Quantidade de Caixas Fechadas e Status da Caixa Atual.

