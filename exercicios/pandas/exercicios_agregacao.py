# --

# ### **Exercícios: Módulo 3 - Análise, Agrupamento e Agregação**

# #### **Contexto**

# Você recebeu dados de vendas que incluem informações sobre o produto vendido, a categoria do produto, o preço e a forma de pagamento utilizada.

# ```python
# import pandas as pd

# dados_vendas = {
#     'ID_Venda': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
#     'Produto': ['Notebook', 'Mouse', 'Monitor', 'Teclado', 'Cadeira Gamer', 'Notebook', 'Webcam', 'Mouse', 'Teclado', 'Monitor'],
#     'Categoria': ['Eletrônicos', 'Acessórios', 'Eletrônicos', 'Acessórios', 'Móveis', 'Eletrônicos', 'Acessórios', 'Acessórios', 'Acessórios', 'Eletrônicos'],
#     'Preco': [4500, 150, 1200, 250, 1800, 4800, 300, 180, 280, 1350],
#     'Forma_Pagamento': ['Cartão de Crédito', 'PIX', 'Cartão de Crédito', 'Boleto', 'Cartão de Crédito', 'PIX', 'PIX', 'Boleto', 'Cartão de Crédito', 'PIX']
# }

# df_vendas = pd.DataFrame(dados_vendas)
# ```

# -----

# ### **Exercícios**

# **1. Estatísticas Descritivas Gerais**

# a) Qual é o **preço médio** de todos os produtos vendidos?
# b) Qual foi o **valor total** arrecadado com todas as vendas? (Soma de todos os preços)
# c) Qual foi o produto **mais caro** e o **mais barato** vendido? (Use `.max()` e `.min()`)

# **2. Contagem de Categorias com `.value_counts()`**

# a) Quantas vendas foram realizadas para cada **`Categoria`** de produto?
# b) Qual foi a **`Forma_Pagamento`** mais utilizada?
# c) Exiba a contagem de vendas por categoria, mas ordenada da categoria **menos** vendida para a **mais** vendida. (Dica: `.value_counts()` tem um parâmetro `ascending`).

# **3. Agrupamento com `.groupby()`**

# a) Qual é o **preço médio** dos produtos para cada **`Categoria`**?
# b) Qual é o **valor total de vendas (soma dos preços)** para cada **`Forma_Pagamento`**?
# c) Para a categoria 'Eletrônicos', qual foi o produto mais caro vendido? (Dica: primeiro filtre o DataFrame, depois use `.max()`).

# **4. Agregação Múltipla com `.agg()`**

# a) Usando `groupby` e `agg`, calcule o preço **médio**, **mínimo** e **máximo** para cada **`Categoria`** de produto, tudo em uma única operação.
# b) Mostre a **quantidade de vendas (`count`)** e o **valor total (`sum`)** para cada **`Forma_Pagamento`**.

# -----

# ### **Desafio**

# Qual **`Categoria`** de produto tem a **maior média de preço**?

# **Dica:** Você pode resolver isso de algumas maneiras. Uma delas é pegar o resultado do exercício 3a e usar o método `.idxmax()` nele.
