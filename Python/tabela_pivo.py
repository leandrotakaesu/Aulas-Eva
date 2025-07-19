import pandas as pd

dados = {
    'Cidade': ['São Paulo', 'Rio de Janeiro', 'São Paulo', 'Belo Horizonte', 'Rio de Janeiro', 'São Paulo'],
    'Categoria': ['Eletrônicos', 'Móveis', 'Acessórios', 'Eletrônicos', 'Acessórios', 'Eletrônicos'],
    'ValorVenda': [1200, 1500, 150, 900, 200, 4500]
}
df_vendas = pd.DataFrame(dados)

# Qual foi o valor total de vendas (sum) de cada Categoria em cada Cidade?

