### Exercícios: Módulo 4 - Praticando com `.pivot_table()`

#### Contexto

# Você recebeu um conjunto de dados de vendas de uma empresa de tecnologia que opera em várias regiões do Brasil. Sua tarefa é criar diferentes relatórios resumidos usando tabelas pivô.


import pandas as pd

dados = {
    'Data': pd.to_datetime(['2025-07-15', '2025-07-15', '2025-07-16', '2025-07-16', '2025-07-17', '2025-07-17', '2025-07-18', '2025-07-18']),
    'Vendedor': ['Ana', 'Bruno', 'Ana', 'Carlos', 'Bruno', 'Ana', 'Carlos', 'Bruno'],
    'Regiao': ['Sudeste', 'Sul', 'Sudeste', 'Sudeste', 'Sul', 'Nordeste', 'Sudeste', 'Nordeste'],
    'Produto': ['Desktop', 'Laptop', 'Desktop', 'Laptop', 'Desktop', 'Laptop', 'Desktop', 'Laptop'],
    'Valor': [3000, 5000, 3200, 4800, 3100, 5500, 2900, 5200]
}
df_vendas = pd.DataFrame(dados)

### **Exercícios**

# 1. Relatório de Vendas por Vendedor e Região (Soma)
# Pergunta: Qual foi o **valor total de vendas de cada **Vendedor** em cada Região?



# 2. Relatório de Preço Médio por Produto e Região (Média)
# Pergunta: Qual foi o valor médio de venda para cada Produto em cada Região?


# 3. Resumo por Vendedor (Múltiplas Agregações)
# Pergunta: Para cada Vendedor, qual foi o valor total vendido  e a quantidade de vendas?


### Desafio: Múltiplos Níveis de Agrupamento

# Pergunta: Qual foi o valor total de vendas para cada Produto, agrupado primeiro por Região e depois por Vendedor?

