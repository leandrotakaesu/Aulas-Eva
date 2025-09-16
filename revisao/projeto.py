# Desafio Final: Análise de E-commerce

# Cenário:
# Você é o analista de dados de uma empresa de e-commerce. Você recebeu três arquivos de dados brutos e separados: vendas, clientes e produtos. A gerência pediu um relatório de desempenho e um modelo preditivo.

# Seu Objetivo: Limpar, integrar, analisar, visualizar e modelar os dados para gerar os insights solicitados.

import pandas as pd
import io

# Dados de Vendas
vendas_csv = """ID_Venda,ID_Produto,ID_Cliente,Data_Venda,Quantidade,Valor_Total
1,101,1,2025-01-05,2,"R$ 1.250,50"
2,102,3,2025-01-07,1,"R$ 89,90"
3,103,2,08/01/2025,5,"R$ 45,00"
4,101,3,2025-01-12,1,"R$ 625,25"
5,104,4,15/01/2025,1,
6,102,2,2025-02-02,3,"R$ 269,70"
7,105,1,2025-02-10,1,"R$ 1.899,00"
8,103,3,21/02/2025,10,"R$ 90,00"
"""

# Dados dos Clientes
clientes_csv = """ID_Cliente,Nome_Cliente,Estado,Data_Cadastro
1,Ana Silva,sp,2022-03-10
2,Bruno Costa,RJ,2021-11-25
3,Carlos Lima, Minas Gerais ,2022-08-01
4,Daniela Souza,SP,2023-01-15
"""

# Dados dos Produtos
produtos_csv = """ID_Produto,Nome_Produto,Categoria,Custo_Unitario
101,Monitor Gamer 27",Eletrônicos,450.50
102,Mousepad Gamer, Acessórios ,25.00
103,Caixa de Som USB,acessórios,7.50
104,Cadeira de Escritório,Móveis,350.00
105,Notebook Pro,eletrônicos,1400.00
"""

# Carregando os dados
df_vendas = pd.read_csv(io.StringIO(vendas_csv))
df_clientes = pd.read_csv(io.StringIO(clientes_csv))
df_produtos = pd.read_csv(io.StringIO(produtos_csv))


# Suas Tarefas
# Parte 1: Limpeza e Preparação (ETL)
# DataFrame de Vendas:

# Limpe a coluna Valor_Total para que ela se torne um tipo numérico (float).

# Há um valor nulo (NaN) em Valor_Total. Decida uma estratégia para tratá-lo e justifique sua escolha.

# A coluna Data_Venda tem formatos mistos (YYYY-MM-DD e DD/MM/YYYY). Unifique toda a coluna para o tipo datetime.

# DataFrame de Clientes:

# Padronize a coluna Estado, removendo espaços extras e convertendo os valores para siglas de 2 letras maiúsculas (ex: ' Minas Gerais ' -> 'MG').

# DataFrame de Produtos:

# Padronize a coluna Categoria, removendo espaços e deixando a primeira letra de cada palavra maiúscula.

# Parte 2: Integração e Análise (BI)
# Merge: Crie um DataFrame final df_completo juntando as três tabelas.

# Engenharia de Features: Crie uma coluna Lucro (baseada no Valor_Total e no Custo_Unitario).

# Análise e Visualização:

# Qual o lucro total por Estado? Crie um gráfico de barras para mostrar o resultado.

# Como o faturamento (Valor_Total) evoluiu ao longo do tempo? Crie um gráfico de linha mostrando o faturamento total por mês.

# Parte 3: Modelagem Preditiva (Machine Learning)
# Objetivo: Criar um modelo que preveja a Categoria de um produto com base no seu Custo_Unitario e no Lucro que ele gera.

# Preparação: Separe o df_completo em X (features) e y (target).

# Pré-processamento: Padronize as features numéricas em X, pois elas têm escalas diferentes.

# Treinamento: Siga o fluxo de 5 passos para treinar um modelo RandomForestClassifier.

# Avaliação: Calcule a acurácia e plote a matriz de confusão para avaliar o desempenho do seu modelo.