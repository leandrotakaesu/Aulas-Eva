# O que é Machine Learning ?
# Ensina o computador a encontrar padrões nos dados para que ele possa fazer previsões sobre dados novos que nunca viu antes.

# O pandas é umaferramente que entende o passado (o que aconteceu)
# O Machine Learning é a ferramenta para prever o futuro (o que provavelmente vai acontecer)

# Scikit-learn
# Tornar o processo de "treinar" e "testar" os modelos, simples e padronizados.

# Se o Pandas construiu a casa com os dados, o Scikit-learn é o engenheiro que instala o "motor de previsões" nela.

# instalacao
# python -m pip install scikit-learn

import pandas as pd
import numpy as np

np.random.seed(42)
tamanho_m2 = np.random.randint(50, 250, size=100)
preco = tamanho_m2 * 5000 + np.random.randint(-80000, 80000, size=100) # Preço = Tamanho * 5k + variação
df_imoveis = pd.DataFrame({'tamanho_m2': tamanho_m2, 'preco': preco})

print(df_imoveis)

# X (Features): São as "causas".  As variáveis que usamos para fazer a previsão (neste caso, o tamanho_m2)
# y (Target): . É o "efeito". A variável que queremos prever (o preco).

X = df_imoveis[['tamanho_m2']]
print(X)
y = df_imoveis['preco']
print(y)

# Nunca testamos o modelo com os mesmos dados que usamos para treiná-lo. 

# Dividimos nossos dados em dois conjuntos:

# Conjunto de Treino (geralmente 70-80%): Usado para o modelo aprender os padrões.

# Conjunto de Teste (geralmente 20-30%): Guardado para o final, para avaliar o desempenho do modelo em dados que ele nunca viu.

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# Dividindo os dados: 80% para treino, 20% para teste
# train_test_split
# Usar random_state=42 é como definir uma "técnica de embaralhamento secreta e numerada"

# Divisão em Dados de Treino e Teste
X_treino, X_teste, y_treino, y_teste = train_test_split(X, y, test_size=0.2, random_state=42)

# Escolha e Criação do Modelo
# Para numeros continuos Regressão Linear
modelo = LinearRegression()

#  Treinamento do Modelo
# Usamos o método .fit() nos dados de treino.

# O modelo "aprende" a relação entre tamanho e preço usando os dados de treino
modelo.fit(X_treino, y_treino)
print("✅ Modelo treinado")


# Avaliação e Previsão
# Agora, usamos os dados de teste (que o modelo nunca viu) para ver se ele aprendeu bem.

from sklearn.metrics import r2_score

# 1. Fazendo previsões nos dados de teste
previsoes = modelo.predict(X_teste)

# 2. Avaliando o desempenho do modelo
score = r2_score(y_teste, previsoes)
print(f"O modelo consegue explicar {score:.2%} da variação dos preços.")

tamanho_novo_imovel = [[150]]
preco_previsto = modelo.predict(tamanho_novo_imovel)
print(f"Previsão de preço para um imóvel de 150 m²: R$ {preco_previsto[0]:,.2f}")
