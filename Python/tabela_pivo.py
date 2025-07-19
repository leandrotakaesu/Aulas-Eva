import pandas as pd

dados = {
    'Cidade': ['São Paulo', 'Rio de Janeiro', 'São Paulo', 'Belo Horizonte', 'Rio de Janeiro', 'São Paulo'],
    'Categoria': ['Eletrônicos', 'Móveis', 'Acessórios', 'Eletrônicos', 'Acessórios', 'Eletrônicos'],
    'ValorVenda': [1200, 1500, 150, 900, 200, 4500]
}
df_vendas = pd.DataFrame(dados)

# Qual foi o valor total de vendas (sum) de cada Categoria em cada Cidade?
tabela_pivo = df_vendas.pivot_table(
    index='Cidade',# coluna cujos valores virarão LINHAS
    columns='Categoria', # coluna cujos valores virarão COLUNAS
    values='ValorVenda',# coluna com os numeros que queremos calcular
    aggfunc='sum',#  A operação que queremos fazer
    fill_value=0# (Opcional) Preenche células vazias (NaN) com 0
)

print(tabela_pivo)