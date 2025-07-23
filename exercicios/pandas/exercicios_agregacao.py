import pandas as pd

dados_vendas = {
  "ID_Venda": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
  "Produto": ["Notebook", "Mouse", "Monitor", "Teclado", "Cadeira Gamer", "Notebook", "Webcam", "Mouse", "Teclado", "Monitor"],
  "Categoria": ["Eletrônicos", "Acessórios", "Eletrônicos", "Acessórios", "Móveis", "Eletrônicos", "Acessórios", "Acessórios", "Acessórios", "Eletrônicos"],
  "Preço": [4500, 150, 1200, 250, 1800, 4800, 300, 180, 280, 1350],
  "Forma_Pagamento": ["Cartão de Crédito", "PIX", "Cartão de Crédito", "Boleto", "Cartão de Crédito", "PIX", "PIX", "Boleto", "Cartão de Crédito", "PIX"]
}

df_vendas = pd.DataFrame(dados_vendas)

# **1. Estatísticas Descritivas Gerais**
# a) Qual é o **preço médio** de todos os produtos vendidos?

preco_medio = df_vendas["Preço"].mean()
print(f"O preço médio dos produtos foi de R$ {preco_medio}")

# b) Qual foi o **valor total** arrecadado com todas as vendas?

valor_total = df_vendas["Preço"].sum()
print(f"O valor total arrecadado foi de R$ {valor_total}")

# c) Qual foi o produto **mais caro** e o **mais barato** vendido? (Use `.max()` e `.min()`)

mais_caro = df_vendas["Preço"].max()
mais_barato = df_vendas["Preço"].min()
print(f"O produto mais caro foi R$ {mais_caro} e o mais barato foi R$ {mais_barato}")

# **2. Contagem de Categorias com `.value_counts()`**
# a) Quantas vendas foram realizadas para cada **`Categoria`** de produto?

contagem_categoria = df_vendas["Categoria"].value_counts()
print("\nQuantidade de vendas por categoria")
print(contagem_categoria)

# b) Qual foi a **`Forma_Pagamento`** mais utilizada?

pagamento_mais_utilizado = df_vendas["Forma_Pagamento"].value_counts().idxmax()
print(f"\nA forma de pagamento mais utilizada foi {pagamento_mais_utilizado}")

# c) Exiba a contagem de vendas por categoria, mas ordenada da categoria **menos** vendida para a **mais** vendida.

contagem_categoria = df_vendas["Categoria"].value_counts(ascending = True)
print("\nQuantidade de vendas por categoria")
print(contagem_categoria)

# **3. Agrupamento com `.groupby()`**
# a) Qual é o **preço médio** dos produtos para cada **`Categoria`**?

preco_medio_categoria = df_vendas.groupby("Categoria")["Preço"].mean()
print("\nPreço médio por categoria")
print(preco_medio_categoria)

# b) Qual é o **valor total de vendas (soma dos preços)** para cada **`Forma_Pagamento`**?

valor_total_pagamento = df_vendas.groupby("Forma_Pagamento")["Preço"].sum()
print("\nValor total por forma de pagamento")
print(valor_total_pagamento)

# c) Para a categoria 'Eletrônicos', qual foi o produto mais caro vendido? (Dica: primeiro filtre o DataFrame, depois use `.max()`).

df_eletronicos = df_vendas[df_vendas["Categoria"] == "Eletrônicos"]
eletronico_mais_caro = df_eletronicos["Preço"].max()
print(f"\nO produto mais caro da categoria eletrônicos foi R$ {eletronico_mais_caro}")

# **4. Agregação Múltipla com `.agg()`**
# a) Usando `groupby` e `agg`, calcule o preço **médio**, **mínimo** e **máximo** para cada **`Categoria`** de produto, tudo em uma única operação.

vendas_por_categoria = df_vendas.groupby("Categoria").agg({"Preço": ["mean", "min", "max"]})
print("\nMédia, mínimo e máximo de vendas por categoria")
print(vendas_por_categoria)

# b) Mostre a **quantidade de vendas (`count`)** e o **valor total (`sum`)** para cada **`Forma_Pagamento`**.

vendas_forma_pagamento = df_vendas.groupby("Forma_Pagamento").agg({"Preço": ["count", "sum"]})
print("\nQuantidade e valor total de vendas por forma de pagamento")
print(vendas_forma_pagamento)

# ### **Desafio**
# Qual **`Categoria`** de produto tem a **maior média de preço**?

preco_medio_categoria = df_vendas.groupby("Categoria")["Preço"].mean()
maior_media_categoria = preco_medio_categoria.idxmax()
print(f"\nA categoria com maior média de preço foi {maior_media_categoria}")