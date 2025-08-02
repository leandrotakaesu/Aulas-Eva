# 4 perguntas 
#
# Evolução ao longo do tempo
# -> Gráfico de Linha
#
# Comparar valores entre grupos e categorias
# -> Gráfico de barras
#
# Entender uma distribuição de uma variavel 
# -> Histograma
#
# Investigar uma relação entre duas variaveis 
# -> Dispersão

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(42)
datas = pd.to_datetime(pd.date_range('2025-01-01', periods=100, freq='D'))
dados = {
    'data_venda': datas,
    'vendedor': np.random.choice(['Ana', 'Bruno', 'Carlos'], 100),
    'preco_produto': np.random.uniform(50, 500, 100).round(2),
    'unidades_vendidas': np.random.randint(1, 6, 100)
}
df_revisao = pd.DataFrame(dados)
df_revisao['faturamento'] = df_revisao['preco_produto'] * df_revisao['unidades_vendidas']

# subplots - moldura com varios espacoes para adicionar imagens, cria uma grade 2x2 -> 4 graficos
# fig - a janela
# axes - array (como uma matriz) axes [linha, coluna]
# ax especifica em qual eixo desenhar
# plt.show()


fig, axes = plt.subplots(nrows=2, ncols=2, figsize=(15,10))
print('Criando a janela para 4 gráficos')


#Como nosso faturamento total evoluiu dia a dia?
faturamento_diario = df_revisao.groupby('data_venda')['faturamento'].sum()
faturamento_diario.plot(
    kind='line',
    title='Evolução do Faturamento Diário',
    ax=axes[0, 0] # Especifica para desenhar no primeiro subplot (canto sup. esquerdo)
)
axes[0,0].set_ylabel("Faturamento (R$)")
# plt.show()

# qual vendedor teve o maior faturamento total no período?

faturamento_vendedor = df_revisao.groupby('vendedor')['faturamento'].sum()
faturamento_vendedor.plot(
    kind='bar',
    title='Faturamento total por Vendedor',
     ax=axes[0, 1]
)
ax=axes[0, 1].set_ylabel("Faturamento Total (R$)")
# plt.show()

# Será que os produtos mais caros vendem menos por transação?

df_revisao.plot(
    kind = "scatter",
    title = "Quantidade vendida por produto",
    x = "preco_produto",
    y = "unidades_vendidas"
)
plt.show()

# Qual a faixa de preço mais comum dos produtos vendidos

df_preco = df_revisao["preco_produto"]
df_preco.plot(
    kind = "hist",
    title = "Faixa de Preço dos produtos",
    y = "preco_produto",
    bins = 5
)
plt.show()