
# Exercícios: Manipulação de Datas e Reamostragem

# Contexto

# Você recebeu os dados de vendas diárias de uma loja. Sua tarefa é organizar esses dados cronologicamente e extrair insights sobre o desempenho de vendas ao longo do tempo.


import pandas as pd
import numpy as np


datas = pd.date_range(start='2025-01-20', periods=40, freq='D')
dados = {
    'data_str': datas.strftime('%Y-%m-%d'),
    'vendas': np.random.randint(100, 500, size=40)
}
df_vendas = pd.DataFrame(dados)


# Exercícios

# 1. Preparação do DataFrame para Análise Temporal (Passos 1 e 2)

# a) A coluna `data_str` está como `object` (texto). Converta-a para o tipo `datetime` e armazene-a em uma nova coluna chamada `data`.

# b) Defina a nova coluna `data` como o índice do DataFrame.

# c) Exiba as 5 primeiras linhas do DataFrame para confirmar que a coluna `data` agora é o índice.

# 2. Seleção e Filtragem por Datas (Slicing - Passo 3)

# Usando o DataFrame com o índice de data que você criou no exercício anterior, realize as seguintes seleções:

# a) Selecione e exiba todas as vendas que ocorreram no dia 31 de janeiro de 2025.

# b) Selecione e exiba todas as vendas que ocorreram na primeira semana de fevereiro de 2025 (do dia 1 ao dia 7).

# 3. Extração de Componentes e Análise (Passo 4)

# a) Crie uma nova coluna no DataFrame chamada `dia_da_semana`, que contenha o nome do dia da semana de cada venda (ex: 'Monday', 'Tuesday', etc.).

# b) Calcule a média de vendas para cada dia da semana.

# c) Qual dia da semana, em média, tem o maior volume de vendas? 

# 4. Reamostragem de Dados (`.resample()` - Passo 5)

# a) Reamostre os dados para encontrar o total de vendas por semana .

# b) Reamostre os dados para encontrar a média de vendas por mês.


#  Desafio

# Crie uma nova coluna chamada `semana_do_mes`, que indica em qual semana do mês a venda ocorreu (1ª, 2ª, 3ª, 4ª ou 5ª).
