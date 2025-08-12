
### Exercícios: Análise Visual com Seaborn

#### Contexto

# Você é um biólogo analisando dados de três espécies diferentes de pinguins. Seu objetivo é usar gráficos para descobrir e comunicar as diferenças e relações entre as características físicas deles.



import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Carregando o dataset 'penguins'
df_penguins = sns.load_dataset('penguins')

# Para simplificar, vamos remover as poucas linhas com dados faltantes
df_penguins.dropna(inplace=True)

# Vamos inspecionar os dados
print("Amostra do DataFrame 'penguins':")
print(df_penguins.head())
df_penguins.info()


# Colunas importantes:

#   * `species`: A espécie do pinguim (Adelie, Chinstrap, Gentoo).
#   * `bill_length_mm`: Comprimento do bico em milímetros.
#   * `flipper_length_mm`: Comprimento da nadadeira em milímetros.
#   * `body_mass_g`: Massa corporal (peso) em gramas.


### Exercícios

# 1. Comparando o Peso das Espécies 
# Pergunta de Negócio: "Queremos saber se existe diferença no peso corporal (`body_mass_g`) entre as diferentes espécies de pinguins. Qual espécie tende a ser a mais pesada e qual tem a maior variação de peso?"

# 2. Relação entre Nadadeiras e Peso
# Pergunta de Negócio: "Existe uma relação entre o comprimento da nadadeira (`flipper_length_mm`) e o peso (`body_mass_g`) de um pinguim? Pinguins com nadadeiras maiores são mais pesados?"

# 3. Entendendo a Distribuição do Comprimento do Bico 
# Pergunta de Negócio: "Qual é a distribuição do comprimento do bico (`bill_length_mm`) de todos os pinguins? Qual a faixa de comprimento mais comum?"


### Desafio: Uma Visão Geral com `pairplot`

# Pergunta de Negócio: "Como todas as variáveis numéricas se relacionam entre si, e como essas relações mudam para cada espécie?"

# Tarefa:
# O Seaborn tem uma função  que cria uma matriz de gráficos:

#   * Gráficos de dispersão para cada par de variáveis.
#   * Histogramas na diagonal para cada variável individual.

# Crie um `pairplot` para o DataFrame `df_penguins`.

