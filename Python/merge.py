import pandas as pd

df_vendas = pd.DataFrame({
    'id_produto': [101, 102, 103, 104],
    'quantidade': [1, 5, 2, 3]
})

df_produtos = pd.DataFrame({
    'id_produto': [101, 102, 105], 
    'nome_produto': ['Monitor', 'Mouse', 'Webcam'],
    'preco': [900, 80, 250]

})

# pd.merge(df_esquerda, df_direita, on='coluna_chave', how='tipo_de_join')
# how: Define quais linhas serão mantidas no resultado final.

# Tipos de Join (how):

# inner: Retorna apenas as linhas onde a chave existe em ambas as tabelas.

# left: Retorna todas as linhas da tabela da esquerda, preenchendo com NaN 
# onde não houver correspondência na direita.

# outer: Retorna todas as linhas de ambas as tabelas.

# Apenas os produtos que estão tanto em vendas quanto no cadastro de produtos
df_inner = pd.merge(df_vendas, df_produtos, on='id_produto', how='inner')
print("## INNER JOIN ##")
print(df_inner)

# Mantém todas as vendas, mesmo que o produto não esteja cadastrado
df_left = pd.merge(df_vendas, df_produtos, on='id_produto', how='left')
print("\n## LEFT JOIN ##")
print(df_left)

# Mantém todos os produtos cadastrados, mesmo que não tenham sido vendidos
df_right = pd.merge(df_vendas, df_produtos, on='id_produto', how='right')
print("\n## RIGHT JOIN ##")
print(df_right)

# Mantém todas as vendas e todos os produtos cadastrados
df_outer = pd.merge(df_vendas, df_produtos, on='id_produto', how='outer')
print("\n## OUTER JOIN ##")
print(df_outer)