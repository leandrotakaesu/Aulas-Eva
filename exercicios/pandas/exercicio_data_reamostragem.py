import pandas as pd
import numpy as np

datas = pd.date_range(start = "2025-01-20", periods = 40, freq = "D")
dados = {
  "data_str": datas.strftime("%Y-%m-%d"),
  "vendas": np.random.randint(100, 500, size=40)
}
df_vendas = pd.DataFrame(dados)

# 1. Preparação do DataFrame para Análise Temporal (Passos 1 e 2)
# a) A coluna `data_str` está como `object` (texto). Converta-a para o tipo `datetime` e armazene-a em uma nova coluna chamada `data`.]

df_vendas["data"] = pd.to_datetime(df_vendas["data_str"])

# b) Defina a nova coluna `data` como o índice do DataFrame.

df_vendas = df_vendas.set_index("data")

# c) Exiba as 5 primeiras linhas do DataFrame para confirmar que a coluna `data` agora é o índice.

print(df_vendas.head())

# 2. Seleção e Filtragem por Datas (Slicing - Passo 3)
# Usando o DataFrame com o índice de data que você criou no exercício anterior, realize as seguintes seleções:
# a) Selecione e exiba todas as vendas que ocorreram no dia 31 de janeiro de 2025.

vendas_31_jan = df_vendas.loc["2025-01-31"]
print("\n")
print(vendas_31_jan)

# b) Selecione e exiba todas as vendas que ocorreram na primeira semana de fevereiro de 2025 (do dia 1 ao dia 7).

vendas_semana_fevereiro = df_vendas.loc["2025-02-01":"2025-02-07"]
print("\n")
print(vendas_semana_fevereiro)

# 3. Extração de Componentes e Análise (Passo 4)
# a) Crie uma nova coluna no DataFrame chamada `dia_da_semana`, que contenha o nome do dia da semana de cada venda (ex: 'Monday', 'Tuesday', etc.).

df_vendas["dia_da_semana"] = df_vendas.index.day_name()
print("\n")
print(df_vendas)

# b) Calcule a média de vendas para cada dia da semana.

vendas_dia_semana = df_vendas.groupby("dia_da_semana")["vendas"].sum()
print("\n")
print(vendas_dia_semana)

# c) Qual dia da semana, em média, tem o maior volume de vendas?

dia_maior_venda = vendas_dia_semana.idxmax()
print("\n")
print(dia_maior_venda)

# 4. Reamostragem de Dados (`.resample()` - Passo 5)
# a) Reamostre os dados para encontrar o total de vendas por semana.

vendas_semanais = df_vendas["vendas"].resample("W").sum()
print("\n")
print(vendas_semanais)

# b) Reamostre os dados para encontrar a média de vendas por mês.

vendas_mensais = df_vendas["vendas"].resample("M").sum()
print("\n")
print(vendas_mensais)

#  Desafio

# Crie uma nova coluna chamada `semana_do_mes`, que indica em qual semana do mês a venda ocorreu (1ª, 2ª, 3ª, 4ª ou 5ª).