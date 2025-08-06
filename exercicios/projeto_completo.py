### ** Análise de E-commerce Completa**

# **Cenário:** Você é o analista de dados de uma plataforma de e-commerce. Você recebeu três arquivos de dados brutos: um com as transações de vendas, um com o cadastro de clientes e outro com o catálogo de produtos. Os dados estão "sujos" e precisam ser limpos, combinados e analisados para gerar um relatório para a gerência.


#### **Passo 0: Os Dados Brutos**

# Use o código abaixo para carregar os três DataFrames.


import pandas as pd
import io

# --- DADOS DE VENDAS ---
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

# --- DADOS DOS CLIENTES ---
clientes_csv = """ID_Cliente,Nome_Cliente,Estado,Data_Cadastro
1,Ana Silva,sp,2022-03-10
2,Bruno Costa,RJ,2021-11-25
3,Carlos Lima, Minas Gerais ,2022-08-01
4,Daniela Souza,SP,2023-01-15
"""

# --- DADOS DOS PRODUTOS ---

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

### **Seu Projeto: O Passo a Passo**

#### **Parte 1: Ingestão e Limpeza de Dados (ETL Básico)**

# 1.  **Limpeza do `df_vendas`:**

#       * A coluna `Data_Venda` tem formatos mistos (`YYYY-MM-DD` e `DD/MM/YYYY`). Converta toda a coluna para o tipo `datetime`. 
#       * A coluna `Valor_Total` é texto. Limpe-a: remova "R$ ", tire espaços, troque a vírgula decimal por ponto e converta para `float`.
#       * Há um valor nulo (`NaN`) em `Valor_Total`. Decida uma estratégia para tratá-lo (ex: preencher com a média da coluna ou remover a linha) e justifique sua escolha.

# 2.  **Limpeza do `df_clientes`:**

#       * Padronize a coluna `Estado`: remova espaços extras e deixe todas as siglas com 2 letras maiúsculas (ex: ' Minas Gerais ' -\> 'MG').
#       * Converta `Data_Cadastro` para `datetime`.

# 3.  **Limpeza do `df_produtos`:**

#       * Padronize a coluna `Categoria`: remova espaços e deixe a primeira letra de cada palavra maiúscula 

#### **Parte 2: Junção (`merge`) e Engenharia de Features**

# 1.  **Crie um DataFrame Completo:** Faça o `merge` das três tabelas para criar um `df_completo` que contenha as informações da venda, os detalhes do produto e os dados do cliente.
# 2.  **Crie Novas Colunas (Engenharia de Features):**
#       * **`Lucro`**: Calcule o lucro de cada venda.
#       * **`Dias_Como_Cliente`**: Para cada venda, calcule há quantos dias o cliente estava cadastrado.
#       * **`Mes_Venda`**: Extraia o mês da `Data_Venda` para facilitar agrupamentos.

#### **Parte 3: Análise e Resposta a Perguntas de Negócio**

# 1.  **Análise Geográfica:** Qual `Estado` teve o maior **lucro** total?
# 2.  **Análise de Produtos:** Qual `Categoria` de produto tem a maior **margem de lucro** média? 
# 3.  **Análise Temporal:** Calcule a **média móvel de 3 dias** do `Valor_Total` das vendas para identificar tendências, suavizando os picos diários. 

#### **Parte 4: Visualização**

# 1.  Crie um **gráfico de barras** mostrando o **Lucro Total por Estado**.
# 2.  Crie um **gráfico de linha** que mostre o `Valor_Total` diário e a `Média Móvel de 3 dias` sobreposta para comparar a tendência com as vendas diárias.
