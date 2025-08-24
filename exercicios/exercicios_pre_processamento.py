# Exercício: Melhorando um Modelo de Previsão de Churn

# Cenário:
# Uma empresa de telecomunicações quer prever a evasão de clientes (churn). Temos dados sobre o tempo de contrato do cliente, sua mensalidade e o tipo de plano. Note como `tempo_cliente_meses` (1-72) e `mensalidade` (50-200) têm escalas bem diferentes.


# import pandas as pd
# import numpy as np


np.random.seed(42)
num_clientes = 200
dados = {
    'tempo_cliente_meses': np.random.randint(1, 72, num_clientes),
    'mensalidade': np.random.uniform(50, 200, num_clientes).round(2),
    'plano': np.random.choice(['Básico', 'Fibra', 'Premium'], num_clientes, p=[0.5, 0.3, 0.2])
}
df_telco = pd.DataFrame(dados)

# Criando a variável alvo 'churn' (1 = Sim, 0 = Não)
# Lógica: Clientes com mensalidades mais altas e pouco tempo de casa têm mais chance de sair
churn_prob = (df_telco['mensalidade'] / 200) - (df_telco['tempo_cliente_meses'] / 150)
df_telco['churn'] = (churn_prob > np.random.uniform(0, 1, num_clientes)).astype(int)


#  Parte 1: O Modelo de Base (Sem Padronização Numérica)

# Primeiro, vamos treinar um modelo apenas convertendo as variáveis categóricas, mas sem padronizar as numéricas.

# 1.  Preparação: Separe o DataFrame em `X` e `y`. O `y` será a coluna `churn`.
# 2.  Encoding: Converta a coluna categórica `plano` em colunas numéricas usando `pd.get_dummies()`. Armazene o resultado em um novo `X_encoded`.
# 3.  Divisão: Divida `X_encoded` e `y` em conjuntos de treino e teste (75% para treino, 25% para teste, `random_state=42`).
# 4.  Treinamento: Treine um `KNeighborsClassifier(n_neighbors=5)` nos dados de treino.
# 5.  Avaliação: Calcule e imprima a acurácia do modelo nos dados de teste. Anote este valor\!


#  Parte 2: O Modelo Otimizado (Com Padronização Numérica)

# Agora, vamos repetir o processo, mas adicionando o passo de padronização (`StandardScaler`) nas colunas numéricas.

# 1.  Reutilize os Dados: Use os `X_treino` e `X_teste` já divididos da Parte 1.
# 2.  Identifique as Colunas: Crie uma lista com os nomes das colunas numéricas que precisam ser padronizadas (`['tempo_cliente_meses', 'mensalidade']`).
# 3.  Crie e Treine o Scaler:
#        Importe `StandardScaler` de `sklearn.preprocessing`.
#        Crie uma instância do `StandardScaler`.
#        Use `.fit_transform()` para aprender e transformar as colunas numéricas do `X_treino`.
# 4.  Transforme os Dados de Teste:
#        Use `.transform()` para aplicar a mesma padronização que foi aprendida no treino às colunas numéricas do `X_teste`.
# 5.  Recrie os DataFrames: Substitua as colunas numéricas originais pelas suas versões padronizadas tanto no `X_treino` quanto no `X_teste`.
# 6.  Treinamento (Novo Modelo): Treine um novo `KNeighborsClassifier(n_neighbors=5)` com os dados de treino totalmente pré-processados.
# 7.  Avaliação (Novo Modelo): Calcule e imprima a acurácia deste novo modelo.
