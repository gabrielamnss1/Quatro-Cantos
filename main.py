# ============================================================================
# ARQUIVO: main.py
# SISTEMA DE GESTÁO - QUATRO CANTOS
# ============================================================================
#
# DESCRIÇÁO:
# Este é o arquivo principal do sistema em modo console/terminal.
# Ele gerencia o menu interativo e permite que o usuário navegue entre
# os diferentes módulos do sistema através de opções numeradas.
#
# FUNCIONALIDADES:
# 1. Exibir menu principal com todas as opções disponíveis
# 2. Capturar a escolha do usuário
# 3. Redirecionar para o módulo correspondente
# 4. Manter o sistema em loop até o usuário decidir sair
# 5. Gerenciar conexão com o banco de dados
#
# MÓDULOS INTEGRADOS:
# - Operacional: Cálculo de capacidade produtiva
# - Estoque Entrada: Cadastro de produtos recebidos
# - Estoque Saída: Registro de vendas e saídas
# - Financeiro: Análise de custos e lucros
# - RH: Gestão de folha de pagamento
#
# ============================================================================

# ============================================================================
# IMPORTAÇÕES DE BIBLIOTECAS PADRÁO DO PYTHON
# ============================================================================
import sys  # Módulo para manipulação de sistema e paths
import os   # Módulo para operações com sistema operacional

# ============================================================================
# CONFIGURAÇÁO DO CAMINHO DE IMPORTAÇÁO
# ============================================================================
# Adiciona o diretório pai ao path de busca do Python
# Isso permite que o Python encontre os módulos na pasta 'src'
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# ============================================================================
# IMPORTAÇÁO DOS MÓDULOS CUSTOMIZADOS DO SISTEMA
# ============================================================================
# Cada módulo representa uma funcionalidade específica do sistema
from src import operacional       # Módulo para cálculos operacionais e produtivos
from src import estoque_entrada   # Módulo para entrada de produtos no estoque
from src import estoque_saida     # Módulo para saída/venda de produtos
from src import financeiro        # Módulo para análises financeiras
from src import rh                # Módulo de Recursos Humanos (RH)
from src.database import init_db, SessionLocal  # Funções para gerenciar o banco de dados