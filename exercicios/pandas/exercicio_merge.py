import pandas as pd

df_vendas = pd.DataFrame({
  "id_venda": [1, 2, 3, 4, 5],
  "id_cliente": [101, 102, 101, 103, 104],
  "id_produto": [201, 202, 203, 201, 204]
})

df_clientes = pd.DataFrame({
  "id_cliente": [101, 102, 103, 105],
  "nome_cliente": ["Ana", "Bruno", "Carlos", "Daniela"]
})

df_produtos = pd.DataFrame({
  "id_produto": [201, 202, 203],
  "nome_produto": ["Monitor", "Teclado", "Mouse"],
  "preço": [1200, 250, 150]
})

# 1. Relatório Básico de Vendas (inner join)
# a) Junte o df_vendas com df_clientes usando a coluna id_cliente. Chame o resultado de df_temp.

df_temp = pd.merge(df_vendas, df_clientes, on = "id_cliente", how = "inner")

# b) Agora, junte o df_temp com df_produtos usando a coluna id_produto para criar o relatório final df_relatorio_vendas.

df_relatorio_vendas = pd.merge(df_temp, df_produtos, on = "id_produto", how = "inner")

# c) Exiba o df_relatorio_vendas. O resultado deve conter apenas as vendas "completas" (onde tanto o cliente quanto o produto estão cadastrados).

print(df_relatorio_vendas)

# 2. Encontrando Clientes Inativos
# a) Faça uma junção entre df_vendas e df_clientes. Pense bem em qual tabela deve ser a da "direita" e qual tipo de how usar para garantir que todos os clientes apareçam no resultado, mesmo os que não têm vendas.

df_clientes_inativos = pd.merge(df_vendas, df_clientes, on = "id_cliente", how = "right")
print("\n")
print(df_clientes_inativos)

# b) No DataFrame resultante, filtre as linhas onde as informações de venda (como id_venda) são nulas (NaN).

df_clientes_inativos = df_clientes_inativos[df_clientes_inativos["id_venda"].isna()]
print("\n")
print(df_clientes_inativos)

# c) Exiba apenas a coluna nome_cliente do resultado filtrado.

print("\n")
print(df_clientes_inativos["nome_cliente"])

# 3. Vendas com Detalhes
# a) Faça uma junção à esquerda (left join) entre df_vendas (à esquerda) e df_produtos (à direita).

df_produtos_inativos = pd.merge(df_vendas, df_produtos, on = "id_produto", how = "left")

# b) Exiba o resultado.

print("\n")
print(df_produtos_inativos)

# Desafio
# Qual o valor total gasto por cada cliente? O relatório final deve conter o nome_cliente e o valor_total_gasto.

df_temp = pd.merge(df_vendas, df_clientes, on = "id_cliente", how = "outer")
df_relatorio_vendas = pd.merge(df_temp, df_produtos, on = "id_produto", how = "outer")
df_relatorio_vendas = df_relatorio_vendas[df_relatorio_vendas["nome_cliente"].notna()]
df_relatorio_vendas = df_relatorio_vendas.groupby("nome_cliente")["preço"].sum()
print("\n")
print(df_relatorio_vendas)