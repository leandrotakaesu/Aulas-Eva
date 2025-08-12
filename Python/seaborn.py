# python3 -m pip install seaborn

# deixa de ser desenhar os graficos 
# passa a ser fazer perguntas para os dados



import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = sns.load_dataset('tips')

#    total_bill   tip     sex smoker  day    time  size
# 0       16.99  1.01  Female     No  Sun  Dinner     2
# 1       10.34  1.66    Male     No  Sun  Dinner     3
# 2       21.01  3.50    Male     No  Sun  Dinner     3
# 3       23.68  3.31    Male     No  Sun  Dinner     2
# 4.       24.59  3.61  Female     No  Sun  Dinner     4

# boxplot
# Um boxplot é excelente para comparar a distribuição de uma variável 
# numérica entre diferentes categorias. Ele mostra a mediana, os quartis e os outliers.

sns.boxplot(x='day', y='total_bill', data=df)
plt.title('Distribuição do Valor da Conta por Dia da Semana')
plt.show()







# 2. Countplot - Contando Categorias
# É como um gráfico de barras que já faz a contagem para você (um .value_counts().plot(kind='bar') em um só comando).

# Pergunta: "Em qual dia da semana o restaurante recebe mais clientes (mesas)?"



plt.figure(figsize=(10, 6))
sns.countplot(x='day', data=df, order=['Thur', 'Fri', 'Sat', 'Sun'])
plt.title('Número de Clientes (Mesas) por Dia da Semana')
plt.show()

# 3. Scatterplot com Regressão (lmplot) - Vendo Relações
# É um gráfico de dispersão aprimorado que já desenha uma linha de tendência para mostrar a correlação entre duas variáveis.

# Pergunta: "Existe uma relação entre o valor total da conta (total_bill) e o valor da gorjeta (tip)?"

sns.lmplot(x='total_bill', y='tip', data=df)
plt.title('Relação entre Valor da Conta e Gorjeta')
plt.show()

# 4. Heatmap - Visualizando Correlações
# Um mapa de calor é perfeito para visualizar uma matriz de dados, como uma matriz de correlação, 
# onde os valores são representados por cores.

# Pergunta: "Como as variáveis numéricas do nosso dataset se correlacionam entre si?"

numeric_df = df.select_dtypes(include=['number'])
correlation_matrix = numeric_df.corr()

sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm')
plt.title('Mapa de Calor da Correlação entre Variáveis')
plt.show()

# -----------
