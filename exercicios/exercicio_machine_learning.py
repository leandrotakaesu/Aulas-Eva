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
# b) Crie a variável y contendo a coluna que você quer prever (o "efeito").

# 2. Divisão em Dados de Treino e Teste
# a) Importe a função train_test_split da biblioteca sklearn.model_selection.
# b) Divida X e y em conjuntos de treino e teste. Use 70% dos dados para treino e 30% para teste.
# c) Use random_state=42 para garantir que sua divisão seja reprodutível.

# 3. Escolha e Criação do Modelo
# a) Importe o modelo LinearRegression da biblioteca sklearn.linear_model.
# b) Crie uma instância do modelo e a armazene em uma variável chamada modelo.

# 4. Treinamento do Modelo
# a) Use o método .fit() para treinar seu modelo com os dados de treino (X_treino e y_treino).

# 5. Avaliação e Previsão
# a) Use o modelo treinado para fazer previsões com os dados de teste (X_teste). Armazene o resultado em uma variável chamada previsoes.
# b) (Desafio) Importe a métrica r2_score de sklearn.metrics. Calcule o score R² comparando os valores reais de teste (y_teste) com as suas previsoes. Imprima o resultado de forma amigável.
# c) Use seu modelo treinado para prever qual seria a venda para um novo investimento de R$ 4.200. Imprima a previsão.