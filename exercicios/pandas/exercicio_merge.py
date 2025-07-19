
# Exercícios: pd.merge() - Combinando Dados de Vendas
# Contexto
# Imagine que você trabalha em um e-commerce e tem três fontes de dados separadas:

# df_vendas: Uma lista de transações, contendo o ID do cliente e o ID do produto vendido.

# df_clientes: O cadastro dos clientes da sua loja.

# df_produtos: O catálogo de produtos que você vende.


import pandas as pd

# Tabela de Vendas
df_vendas = pd.DataFrame({
    'id_venda': [1, 2, 3, 4, 5],
    'id_cliente': [101, 102, 101, 103, 104], 
    'id_produto': [201, 202, 203, 201, 204] 
})

# Tabela de Clientes
df_clientes = pd.DataFrame({
    'id_cliente': [101, 102, 103, 105],
    'nome_cliente': ['Ana', 'Bruno', 'Carlos', 'Daniela']
})

# Tabela de Produtos
df_produtos = pd.DataFrame({
    'id_produto': [201, 202, 203], 
    'nome_produto': ['Monitor', 'Teclado', 'Mouse'],
    'preco': [1200, 250, 150]
})

# Exercícios
# 1. Relatório Básico de Vendas (inner join)

# Objetivo: Criar um relatório que mostre o nome do cliente e o nome do produto para cada venda.

# a) Junte o df_vendas com df_clientes usando a coluna id_cliente. Chame o resultado de df_temp.
# b) Agora, junte o df_temp com df_produtos usando a coluna id_produto para criar o relatório final df_relatorio_vendas.
# c) Exiba o df_relatorio_vendas. O resultado deve conter apenas as vendas "completas" (onde tanto o cliente quanto o produto estão cadastrados).


# 2. Encontrando Clientes Inativos

# Objetivo: Descobrir quais clientes estão cadastrados na loja, mas nunca fizeram uma compra.

# a) Faça uma junção entre df_vendas e df_clientes. Pense bem em qual tabela deve ser a da "direita" e qual tipo de how usar para garantir que todos os clientes apareçam no resultado, mesmo os que não têm vendas.
# b) No DataFrame resultante, filtre as linhas onde as informações de venda (como id_venda) são nulas (NaN).
# c) Exiba apenas a coluna nome_cliente do resultado filtrado.

# 3. Vendas com Detalhes 

# Objetivo: Criar um relatório que mostre todas as vendas, mas que também inclua os nomes dos produtos, mesmo que um produto vendido não esteja mais no catálogo.

# a) Faça uma junção à esquerda (left join) entre df_vendas (à esquerda) e df_produtos (à direita).
# b) Exiba o resultado.


# Desafio
# Qual o valor total gasto por cada cliente? O relatório final deve conter o nome_cliente e o valor_total_gasto.


