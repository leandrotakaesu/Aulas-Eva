# Exercício 1: Tendência de Acessos ao Longo do Tempo
# Cenário: Você tem os dados diários de acessos a um site durante o mês de junho.

import pandas as pd
import numpy as np

np.random.seed(10) # Para gerar sempre os mesmos dados
datas = pd.date_range(start='2025-06-01', end='2025-06-30', freq='D')
acessos = np.random.randint(1000, 2500, size=len(datas)) + np.arange(len(datas)) * 50
df_acessos = pd.DataFrame({'Data': datas, 'Acessos': acessos}).set_index('Data')

# Pergunta de Negócio: "Queremos ver a tendência de acessos ao nosso site durante o mês de Junho. Houve picos ou quedas em dias específicos? O tráfego geral está crescendo, diminuindo ou estável?"

# Sua Tarefa:

# Qual gráfico usar?

# Por quê?

# Escreva o código.

# Exercício 2: Comparação de Desempenho de Vendas
# Cenário: Você tem os dados consolidados do total de vendas (em milhões) para diferentes produtos de uma empresa.

# Python

# df_produtos = pd.DataFrame({
#     'Produto': ['Notebook', 'Desktop', 'Celular', 'Tablet', 'Smartwatch'],
#     'Vendas_Milhoes': [450, 380, 620, 210, 150]
# }).set_index('Produto')
# Pergunta de Negócio: "Precisamos comparar visualmente o desempenho de vendas de cada produto. Qual produto é o campeão de vendas e quais têm o desempenho mais fraco?"

# Sua Tarefa:

# Qual gráfico usar?

# Por quê?

# Escreva o código.

# Exercício 3: Análise da Distribuição de Preços
# Cenário: Você tem uma lista com os preços de 200 imóveis que foram vendidos em uma determinada cidade.

# Python

# np.random.seed(42)
# precos = np.random.normal(loc=500000, scale=150000, size=200).astype(int)
# df_imoveis = pd.DataFrame({'Preco_Venda': precos})
# Pergunta de Negócio: "Qual é a faixa de preço mais comum para os imóveis vendidos? Os preços se concentram em torno de um valor central ou estão muito espalhados? Existem muitos imóveis muito caros ou muito baratos (outliers)?"

# Sua Tarefa:

# Qual gráfico usar?

# Por quê?

# Escreva o código.

# Exercício 4: Relação entre Investimento e Retorno
# Cenário: Você tem dados de várias campanhas de marketing, mostrando o valor investido e o retorno (receita gerada) para cada uma.

# Python

np.random.seed(1)
investimento = np.random.randint(1000, 10000, size=50)
receita = investimento * np.random.uniform(2.5, 4.0, size=50) + np.random.randint(-1000, 1000, size=50)
df_campanhas = pd.DataFrame({'Investimento': investimento, 'Receita': receita})

# Pergunta de Negócio: "Existe uma relação entre o valor que investimos em uma campanha e a receita que ela gera? Quanto maior o investimento, maior a receita?"

# Sua Tarefa:

# Qual gráfico usar?

# Por quê?

# Escreva o código.