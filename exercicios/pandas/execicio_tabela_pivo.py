import pandas as pd

dados = {
  "Data": pd.to_datetime(["2025-07-15", "2025-07-15", "2025-07-16", "2025-07-16", "2025-07-17", "2025-07-17", "2025-07-18", "2025-07-18"]),
  "Vendedor": ["Ana", "Bruno", "Ana", "Carlos", "Bruno", "Ana", "Carlos", "Bruno"],
  "Região": ["Sudeste", "Sul", "Sudeste", "Sudeste", "Sul", "Nordeste", "Sudeste", "Nordeste"],
  "Produto": ["Desktop", "Laptop", "Desktop", "Laptop", "Desktop", "Laptop", "Desktop", "Laptop"],
  "Valor": [3000, 5000, 3200, 4800, 3100, 5500, 2900, 5200]
}

df_vendas = pd.DataFrame(dados)

# 1. Relatório de Vendas por Vendedor e Região (Soma)
# Pergunta: Qual foi o **valor total de vendas de cada **Vendedor** em cada Região?

tabela_pivo = df_vendas.pivot_table(
  index = "Vendedor",
  columns = "Região",
  values = "Valor",
  aggfunc = "sum",
  fill_value = 0
)
print(tabela_pivo)

# 2. Relatório de Preço Médio por Produto e Região (Média)
# Pergunta: Qual foi o valor médio de venda para cada Produto em cada Região?

tabela_pivo = df_vendas.pivot_table(
  index = "Produto",
  columns = "Região",
  values = "Valor",
  aggfunc = "mean",
  fill_value = 0
)
print("\n")
print(tabela_pivo)

# 3. Resumo por Vendedor (Múltiplas Agregações)
# Pergunta: Para cada Vendedor, qual foi o valor total vendido  e a quantidade de vendas?

vendas_por_vendedor = df_vendas.groupby("Vendedor").agg({"Valor": ["sum", "count"]})
print("\n")
print(vendas_por_vendedor)

tabela_pivo = df_vendas.pivot_table(
  index = "Vendedor",
  values = "Valor",
  aggfunc = ["sum", "count"],
  fill_value = 0
)
print("\n")
print(tabela_pivo)

### Desafio: Múltiplos Níveis de Agrupamento
# Pergunta: Qual foi o valor total de vendas para cada Produto, agrupado primeiro por Região e depois por Vendedor?

tabela_pivo = df_vendas.pivot_table(
  index = ["Região", "Vendedor"],
  columns = "Produto",
  values = "Valor",
  aggfunc = "sum",
  fill_value = 0
)
print("\n")
print(tabela_pivo)