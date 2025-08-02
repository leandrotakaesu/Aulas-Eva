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

# # Código para plotar o gráfico de linhas
# plt.style.use('seaborn-v0_8-whitegrid')
# plt.figure(figsize=(12, 6))
# plt.plot(df_acessos.index, df_acessos['Acessos'], marker='o', linestyle='-')

# # Adicionando título e rótulos
# plt.title('Tendência de Acessos ao Site em Junho de 2025')
# plt.xlabel('Data')
# plt.ylabel('Número de Acessos')

# # Melhorando a visualização
# plt.xticks(rotation=45)
# plt.tight_layout()

# plt.show()

# Exercício 2: Comparação de Desempenho de Vendas
# Cenário: Você tem os dados consolidados do total de vendas (em milhões) para diferentes produtos de uma empresa.

df_produtos = pd.DataFrame({
    'Produto': ['Notebook', 'Desktop', 'Celular', 'Tablet', 'Smartwatch'],
    'Vendas_Milhoes': [450, 380, 620, 210, 150]
}).set_index('Produto')

# Pergunta de Negócio: "Precisamos comparar visualmente o desempenho de vendas de cada produto. Qual produto é o campeão de vendas e quais têm o desempenho mais fraco?"
# Qual gráfico usar?
# Escreva o código.

# # Ordena os dados para melhor visualização
# df_produtos_sorted = df_produtos.sort_values('Vendas_Milhoes', ascending=False)

# # Cria o gráfico de barras
# plt.style.use('seaborn-v0_8-whitegrid')
# plt.figure(figsize=(10, 6))
# bars = plt.bar(df_produtos_sorted.index, df_produtos_sorted['Vendas_Milhoes'], color='skyblue')

# # Adiciona os valores no topo de cada barra
# for bar in bars:
#     yval = bar.get_height()
#     plt.text(bar.get_x() + bar.get_width()/2.0, yval, f'{int(yval)}M', va='bottom', ha='center') # M for Milhões

# # Adiciona título e rótulos
# plt.title('Total de Vendas por Produto')
# plt.xlabel('Produto')
# plt.ylabel('Vendas (em Milhões de R$)')
# plt.ylim(0, df_produtos_sorted['Vendas_Milhoes'].max() * 1.1) # Ajusta o limite do eixo y

# plt.show()

# Exercício 3: Análise da Distribuição de Preços
# Cenário: Você tem uma lista com os preços de 200 imóveis que foram vendidos em uma determinada cidade.

np.random.seed(42)
precos = np.random.normal(loc=500000, scale=150000, size=200).astype(int)
df_imoveis = pd.DataFrame({'Preco_Venda': precos})

# Pergunta de Negócio: "Qual é a faixa de preço mais comum para os imóveis vendidos? Os preços se concentram em torno de um valor central ou estão muito espalhados? Existem muitos imóveis muito caros ou muito baratos (outliers)?"
# Qual gráfico usar?
# Escreva o código.

# # Calcula a média para adicionar uma linha de referência
# media_preco = df_imoveis['Preco_Venda'].mean()

# # Cria o histograma
# plt.style.use('seaborn-v0_8-whitegrid')
# plt.figure(figsize=(10, 6))
# plt.hist(df_imoveis['Preco_Venda'], bins=20, color='c', edgecolor='black', alpha=0.7)

# # Adiciona uma linha vertical para a média
# plt.axvline(media_preco, color='red', linestyle='dashed', linewidth=2)
# plt.text(media_preco * 1.02, plt.ylim()[1] * 0.9, f'Média: R$ {media_preco:,.0f}'.replace(',', '.'), color='red')

# # Adiciona título e rótulos
# plt.title('Distribuição dos Preços de Venda dos Imóveis')
# plt.xlabel('Preço de Venda (R$)')
# plt.ylabel('Frequência (Número de Imóveis)')

# plt.show()

# Exercício 4: Relação entre Investimento e Retorno
# Cenário: Você tem dados de várias campanhas de marketing, mostrando o valor investido e o retorno (receita gerada) para cada uma.

np.random.seed(1)
investimento = np.random.randint(1000, 10000, size=50)
receita = investimento * np.random.uniform(2.5, 4.0, size=50) + np.random.randint(-1000, 1000, size=50)
df_campanhas = pd.DataFrame({'Investimento': investimento, 'Receita': receita})

# Pergunta de Negócio: "Existe uma relação entre o valor que investimos em uma campanha e a receita que ela gera? Quanto maior o investimento, maior a receita?"
# Qual gráfico usar?
# Escreva o código.

# # Cria o gráfico de dispersão
# plt.style.use('seaborn-v0_8-whitegrid')
# plt.figure(figsize=(10, 6))
# plt.scatter(df_campanhas['Investimento'], df_campanhas['Receita'], alpha=0.7, edgecolors='b')

# # Adiciona uma linha de tendência para visualizar melhor a relação
# m, b = np.polyfit(df_campanhas['Investimento'], df_campanhas['Receita'], 1)
# plt.plot(df_campanhas['Investimento'], m * df_campanhas['Investimento'] + b, color='red', linewidth=2)

# # Adiciona título e rótulos
# plt.title('Relação entre Investimento e Receita nas Campanhas')
# plt.xlabel('Investimento (R$)')
# plt.ylabel('Receita Gerada (R$)')

# plt.show()