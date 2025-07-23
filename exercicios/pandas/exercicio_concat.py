import pandas as pd

dados_a = {
  "Vendedor": ["Ana", "Bruno", "Ana", "Carlos"],
  "Categoria": ["Notebook", "Acessório", "Notebook", "Celular"],
  "Valor_Venda": [4500, 250, 5200, 3500]
}
df_loja_a = pd.DataFrame(dados_a)
df_loja_a["Loja"] = "Loja A"

dados_b = {
  "Vendedor": ["Sofia", "Ana", "Bruno", "Sofia"],
  "Categoria": ["Celular", "Acessório", "Acessório", "Notebook"],
  "Valor_Venda": [3800, 300, 280, 4900]
}
df_loja_b = pd.DataFrame(dados_b)
df_loja_b["Loja"] = "Loja B"

# **1. Concatenando os Dados (`pd.concat`)**
# a) Use `pd.concat()` para criar um único DataFrame chamado `df_vendas_total` que contenha todas as vendas das duas lojas.

df_vendas_total = pd.concat([df_loja_a, df_loja_b], ignore_index = True)

# b) Certifique-se de que o índice do novo DataFrame (`df_vendas_total`) seja contínuo, começando do 0.

print("Vendas Totais")
print(df_vendas_total)

# c) Exiba as 5 primeiras linhas do novo DataFrame para conferir o resultado.

print("\nVendas Totais - 5 primeiras linhas")
print(df_vendas_total.head(5))

# **2. Análise Geral do DataFrame Combinado**
# a) Qual o valor **total** de vendas, somando as duas lojas?

soma_total = df_vendas_total["Valor_Venda"].sum()
print(f"\nO valor total das vendas foi de R$ {soma_total}")

# b) Qual a **média** de valor por venda?

media_vendas = df_vendas_total["Valor_Venda"].mean()
print(f"\nO valor médio das vendas foi de R$ {media_vendas}")

# c) Quantas vendas foram realizadas no total?

qtd_vendas = df_vendas_total["Valor_Venda"].count()
print(f"\nA quantidade de vendas realizadas foi de {qtd_vendas}")

# **3. Análise por Grupos (`groupby`)**
# a) Qual foi o valor total de vendas (soma) por **`Loja`**?

vendas_por_loja = df_vendas_total.groupby("Loja")["Valor_Venda"].sum()
print("\nVendas por loja")
print(vendas_por_loja)

# b) Qual foi o valor médio de venda por **`Categoria`** de produto (considerando ambas as lojas)?

media_por_categoria = df_vendas_total.groupby("Categoria")["Valor_Venda"].mean()
print("\nMédia de vendas por categoria")
print(media_por_categoria)

# c) Qual **`Vendedor`** teve o maior faturamento total (soma de todas as suas vendas)?

total_por_vendedor = df_vendas_total.groupby("Vendedor")["Valor_Venda"].sum()
vendedor_maior_faturamento = total_por_vendedor.idxmax()
print(f"\nO vendedor com maior faturamento foi {vendedor_maior_faturamento}")

# **4. Contagem e Agregação Múltipla (`value_counts` e `agg`)**
# a) Quantas vendas cada **`Vendedor`** realizou no total?

vendas_por_vendedor = df_vendas_total["Vendedor"].value_counts()
print("\nQuantidade de vendas por vendedor")
print(vendas_por_vendedor)

# b) Usando `groupby` e `.agg()`, mostre para cada **`Categoria`** o **número de vendas** (`count`) e o **valor da venda média** (`mean`).

vendas_por_categoria = df_vendas_total.groupby("Categoria").agg({"Valor_Venda": ["count", "mean"]})
print("\nQuantidade e média de vendas por categoria")
print(vendas_por_categoria)

# ### **Desafio**
# Em qual **`Loja`** a categoria **'Notebook'** teve a maior média de preço de venda?

df_notebook = df_vendas_total[df_vendas_total["Categoria"] == "Notebook"]
notebook_por_loja = df_notebook.groupby("Loja")["Valor_Venda"].mean()
maior_notebook = notebook_por_loja.idxmax()
print(f"\nA maior média da categoria notebook foi na loja {maior_notebook}")