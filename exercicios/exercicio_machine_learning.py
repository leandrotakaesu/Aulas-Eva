# Cenário: Você é analista em uma empresa e recebeu dados sobre o investimento em marketing e as vendas resultantes em diferentes meses. Seu objetivo é criar um modelo que possa prever as vendas futuras com base no valor que se pretende investir.

import pandas as pd
import numpy as np

# Gerando dados de exemplo
np.random.seed(0)
investimento_marketing = np.random.randint(1000, 5000, size=50)
vendas = investimento_marketing * 3.5 + np.random.randint(-1500, 1500, size=50)
df_vendas = pd.DataFrame({
    'investimento_marketing': investimento_marketing,
    'vendas': vendas
})


# Sua Tarefa: Siga os 5 Passos do Machine Learning
# 1. Preparação dos Dados (Definir X e y)
# a) Crie a variável X contendo a coluna que será usada para prever (a "causa").

X = df_vendas[['investimento_marketing']]

# b) Crie a variável y contendo a coluna que você quer prever (o "efeito").

y = df_vendas['vendas']

# 2. Divisão em Dados de Treino e Teste
# a) Importe a função train_test_split da biblioteca sklearn.model_selection.

from sklearn.model_selection import train_test_split

# b) Divida X e y em conjuntos de treino e teste. Use 70% dos dados para treino e 30% para teste.

X_treino, X_teste, y_treino, y_teste = train_test_split(X, y, test_size = 0.3, random_state = 42)

# c) Use random_state=42 para garantir que sua divisão seja reprodutível.

# 3. Escolha e Criação do Modelo
# a) Importe o modelo LinearRegression da biblioteca sklearn.linear_model.

from sklearn.linear_model import LinearRegression

# b) Crie uma instância do modelo e a armazene em uma variável chamada modelo.

modelo = LinearRegression()

# 4. Treinamento do Modelo
# a) Use o método .fit() para treinar seu modelo com os dados de treino (X_treino e y_treino).

modelo.fit(X_treino, y_treino)

# 5. Avaliação e Previsão
# a) Use o modelo treinado para fazer previsões com os dados de teste (X_teste).
# Armazene o resultado em uma variável chamada previsoes.

from sklearn.metrics import r2_score

previsoes = modelo.predict(X_teste)

# b) (Desafio) Importe a métrica r2_score de sklearn.metrics.
# Calcule o score R² comparando os valores reais de teste (y_teste) com as suas previsoes.
# Imprima o resultado de forma amigável.

score = r2_score(y_teste, previsoes)
print(f"O modelo consegue explicar {score:.2%} da variação das vendas.")

# c) Use seu modelo treinado para prever qual seria a venda para um novo investimento de R$ 4.200. Imprima a previsão.

novo_investimento = [[4200]]
venda_prevista = modelo.predict(novo_investimento)
print(f"Previsão de preço para um investimento de R$ 4.200,00: R$ {venda_prevista[0]:,.2f}")



# Preparação: Separamos os dados em X (o que usamos para prever) e y (o que queremos prever). É crucial que X seja um DataFrame (com colchetes duplos), pois os modelos do Scikit-learn esperam uma entrada 2D.

# Divisão: Usamos train_test_split para criar os conjuntos de treino e teste. Isso nos permite avaliar o modelo de forma honesta, testando-o com dados que ele nunca viu durante o treinamento. random_state=42 garante que a divisão seja sempre a mesma.

# Criação do Modelo: modelo = LinearRegression() simplesmente cria um "cérebro" de regressão linear vazio, pronto para aprender.

# Treinamento: modelo.fit(X_treino, y_treino) é a etapa de aprendizado. O modelo analisa a relação entre investimento e vendas nos dados de treino e "desenha" a melhor linha reta que descreve essa relação.

# Avaliação:

# .predict(X_teste) usa a linha aprendida para prever os valores de vendas para os dados de teste.

# r2_score compara as previsões com os valores reais (y_teste) e nos dá uma nota de 0 a 1. Um score de 97.87% é excelente, indicando que nosso modelo é muito bom em prever as vendas com base no investimento.

# Para prever um novo valor, precisamos passá-lo em um formato 2D, por isso usamos [[4200]]. O modelo então aplica a fórmula que aprendeu para nos dar a previsão de vendas.



import matplotlib as plt

