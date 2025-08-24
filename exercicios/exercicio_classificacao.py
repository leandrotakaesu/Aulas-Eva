
### **Exercício: Modelo de Risco de Crédito**


# Você trabalha em uma fintech e sua equipe quer construir um modelo simples para prever o risco de um cliente não pagar um empréstimo (`inadimplente`). Você recebeu dados sobre a idade, a renda e o histórico de empréstimos de clientes anteriores.


import pandas as pd
import numpy as np

# Gerando dados de exemplo para 200 clientes
np.random.seed(2025)
num_clientes = 200
dados = {
    'idade': np.random.randint(22, 65, num_clientes),
    'renda_anual_mil': np.random.randint(30, 200, num_clientes),
    'num_emprestimos_anteriores': np.random.randint(0, 10, num_clientes),
}
df_credito = pd.DataFrame(dados)

# Criando a variável alvo 'inadimplente' (1 = Sim, 0 = Não) com base em uma lógica
# Risco maior: baixa renda, muitos empréstimos
probabilidade = (df_credito['num_emprestimos_anteriores'] / 10) - (df_credito['renda_anual_mil'] / 400)
df_credito['inadimplente'] = (probabilidade > np.random.uniform(0, 0.8, num_clientes)).astype(int)


### **Sua Tarefa: Construa e Avalie um Modelo de Classificação**

# Sua tarefa é treinar um modelo **K-Nearest Neighbors (K-NN)** para prever se um cliente se tornará `inadimplente` (1) ou não (0).

# **1. Preparação dos Dados**
# a) Separe o DataFrame em `X` (as features/causas) e `y` (o target/efeito:).

# **2. Divisão em Treino e Teste**
# a) Divida os dados em 75% para treino e 25% para teste.
# b) Use `random_state=42` para garantir que a divisão seja sempre a mesma.

# **3. Escolha e Criação do Modelo**
# a) Crie uma instância do `KNeighborsClassifier`. Para este exercício, use 7 vizinhos (`n_neighbors=7`).

# **4. Treinamento do Modelo**
# a) Treine o modelo usando os dados de treino (`X_treino`, `y_treino`).

# **5. Avaliação do Desempenho**
# a) Faça as previsões no conjunto de teste.
# b) Calcule e imprima a **acurácia** do modelo.
# c) Gere e plote a **matriz de confusão** com o Seaborn para ver os detalhes dos acertos e erros do modelo.

# -----

# Desafio: Previsão Prática

# Use o modelo que você treinou para prever o risco para os dois novos perfis de clientes abaixo. O modelo classificará cada um como `0` (bom pagador) ou `1` (risco de inadimplência)?

#   Cliente A:** 45 anos, renda anual de R$ 80 mil, 1 empréstimo anterior.
#   Cliente B:** 28 anos, renda anual de R$ 45 mil, 6 empréstimos anteriores.
