import pandas as pd
import matplotlib.pyplot as plt

dados = {
    'Mes': pd.to_datetime(['2025-01-01', '2025-02-01', '2025-03-01', '2025-04-01']),
    'Vendas_Eletronicos': [20000, 22000, 28000, 25000],
    'Vendas_Roupas': [15000, 18000, 14000, 21000]
}
df = pd.DataFrame(dados).set_index('Mes')

# parametro kind, que define o tipo do grafico que vai ser criado.


# grafico de linha
df.plot(
    kind='line',
    title='Evolução das vendas mensais',
    xlabel='Mês',
    ylabel='Valor da Venda',
)

plt.show()

# grafico de barra 
#kind='bar',


# histograma
#kind='hist',

# grafico de dispersao
# kind='scatter',
