
# ### **Exercícios: Concatenando e Analisando Dados**

# #### **Contexto**

# Imagine que uma empresa tem duas filiais, "Loja A" e "Loja B". Você recebeu os dados de vendas de cada uma em arquivos (DataFrames) separados. Sua primeira tarefa é juntar esses dados para, em seguida, analisá-los como um todo.

# **DataFrames Iniciais:**

# ```python
# import pandas as pd

# # Vendas da primeira filial
# dados_a = {
#     'Vendedor': ['Ana', 'Bruno', 'Ana', 'Carlos'],
#     'Categoria': ['Notebook', 'Acessório', 'Notebook', 'Celular'],
#     'Valor_Venda': [4500, 250, 5200, 3500]
# }
# df_loja_a = pd.DataFrame(dados_a)
# # Adicionando uma coluna para identificar a origem dos dados
# df_loja_a['Loja'] = 'Loja A'

# # Vendas da segunda filial
# dados_b = {
#     'Vendedor': ['Sofia', 'Ana', 'Bruno', 'Sofia'],
#     'Categoria': ['Celular', 'Acessório', 'Acessório', 'Notebook'],
#     'Valor_Venda': [3800, 300, 280, 4900]
# }
# df_loja_b = pd.DataFrame(dados_b)
# # Adicionando uma coluna para identificar a origem dos dados
# df_loja_b['Loja'] = 'Loja B'
# ```

# -----

# ### **Exercícios**

# **1. Concatenando os Dados (`pd.concat`)**
# a) Use `pd.concat()` para criar um único DataFrame chamado `df_vendas_total` que contenha todas as vendas das duas lojas.
# b) Certifique-se de que o índice do novo DataFrame (`df_vendas_total`) seja contínuo, começando do 0.
# c) Exiba as 5 primeiras linhas do novo DataFrame para conferir o resultado.
# 💡 **Dica:** O parâmetro `ignore_index=True` do `concat` faz o item (b) para você.

# **2. Análise Geral do DataFrame Combinado (Revisão)**
# Com o `df_vendas_total` criado, responda:
# a) Qual o valor **total** de vendas, somando as duas lojas? (Use `.sum()`)
# b) Qual a **média** de valor por venda? (Use `.mean()`)
# c) Quantas vendas foram realizadas no total? (Use o atributo `.shape` ou a função `len()`).

# **3. Análise por Grupos (`groupby`)**
# Agora, use o `df_vendas_total` para fazer análises agrupadas e responder às seguintes perguntas:
# a) Qual foi o valor total de vendas (soma) por **`Loja`**?
# b) Qual foi o valor médio de venda por **`Categoria`** de produto (considerando ambas as lojas)?
# c) Qual **`Vendedor`** teve o maior faturamento total (soma de todas as suas vendas)? (Dica: agrupe por vendedor, some os valores e depois use `.idxmax()`).

# **4. Contagem e Agregação Múltipla (`value_counts` e `agg`)**
# a) Quantas vendas cada **`Vendedor`** realizou no total? (Use `.value_counts()`).
# b) Usando `groupby` e `.agg()`, mostre para cada **`Categoria`** o **número de vendas** (`count`) e o **valor da venda média** (`mean`).

# -----

# ### **Desafio**

# Em qual **`Loja`** a categoria **'Notebook'** teve a maior média de preço de venda?



