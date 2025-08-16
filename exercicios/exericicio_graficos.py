# Exercício 1: Tendência de Acessos ao Longo do Tempo
# Cenário: Você tem os dados diários de acessos a um site durante o mês de junho.

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(10) # Para gerar sempre os mesmos dados
datas = pd.date_range(start='2025-06-01', end='2025-06-30', freq='D')
acessos = np.random.randint(1000, 2500, size=len(datas)) + np.arange(len(datas)) * 50
df_acessos = pd.DataFrame({'Data': datas, 'Acessos': acessos}).set_index('Data')

# Pergunta de Negócio: "Queremos ver a tendência de acessos ao nosso site durante o mês de Junho. Houve picos ou quedas em dias específicos? O tráfego geral está crescendo, diminuindo ou estável?"
# Qual gráfico usar?
# Escreva o código.

df_acessos_junho = df_acessos['Acessos']
df_acessos_junho.plot(
    kind='line',
    title='Acessos ao Site por Dia',
    xlabel='Data',
    ylabel='Acessos'
)
plt.show()

# Exercício 2: Comparação de Desempenho de Vendas
# Cenário: Você tem os dados consolidados do total de vendas (em milhões) para diferentes produtos de uma empresa.

df_produtos = pd.DataFrame({
    'Produto': ['Notebook', 'Desktop', 'Celular', 'Tablet', 'Smartwatch'],
    'Vendas_Milhoes': [450, 380, 620, 210, 150]
}).set_index('Produto')

# Pergunta de Negócio: "Precisamos comparar visualmente o desempenho de vendas de cada produto. Qual produto é o campeão de vendas e quais têm o desempenho mais fraco?"
# Qual gráfico usar?
# Escreva o código.

df_produtos.plot(
    kind='bar',
    title='Vendas de Produtos',
    xlabel='Produto',
    ylabel='Vendas (em milhões)'
)

plt.show()

# Exercício 3: Análise da Distribuição de Preços
# Cenário: Você tem uma lista com os preços de 200 imóveis que foram vendidos em uma determinada cidade.

np.random.seed(42)
precos = np.random.normal(loc=500000, scale=150000, size=200).astype(int)
df_imoveis = pd.DataFrame({'Preco_Venda': precos})

# Pergunta de Negócio: "Qual é a faixa de preço mais comum para os imóveis vendidos? Os preços se concentram em torno de um valor central ou estão muito espalhados? Existem muitos imóveis muito caros ou muito baratos (outliers)?"
# Qual gráfico usar?
# Escreva o código.

df_imoveis.plot(
    kind = "hist",
    title = "Quantidade de imóveis por faixa de preço",
    y = "Preco_Venda",
    bins = 20,
    xlabel = "Faixa de Preço",
    ylabel = "Quantidade de Imóveis"
)
plt.show()

# Exercício 4: Relação entre Investimento e Retorno
# Cenário: Você tem dados de várias campanhas de marketing, mostrando o valor investido e o retorno (receita gerada) para cada uma.

np.random.seed(1)
investimento = np.random.randint(1000, 10000, size=50)
receita = investimento * np.random.uniform(2.5, 4.0, size=50) + np.random.randint(-1000, 1000, size=50)
df_campanhas = pd.DataFrame({'Investimento': investimento, 'Receita': receita})

# Pergunta de Negócio: "Existe uma relação entre o valor que investimos em uma campanha e a receita que ela gera? Quanto maior o investimento, maior a receita?"
# Qual gráfico usar?
# Escreva o código.

df_campanhas.plot(
    kind = "scatter",
    title = "Investimento em campanha x Receita",
    x = "Investimento",
    y = "Receita",
    xlabel = "Investimento",
    ylabel = "Receita"
)

plt.show()