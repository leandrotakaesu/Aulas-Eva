# #Revisão

# Manipulação de dados com pandas

# iloc -> seleciona dados pela POSIÇÃO numérica (inteira) da linha e da coluna, começando em 0.

# loc -> seleciona dados pelo RÓTULO (nome) do índice e da coluna.

# Filtros

# Filtrar por idade 

# df_clientes[df_clientes['idade']> 30]

# Converter um texto em colunas numericas

# pd.get_dummies() -> -> 
# 'plano': ['Básico', 'Premium']) 
#  (  Plano_Básico: [1, 0], 
#     Plano_Premium: [0, 1])

# Pergunta: Descobrir o valor médio de venda por categoria.

# df.groupby('Categoria')['Valor_Venda'].mean()

# Visualização de Dados com Seaborn

# Cenário A (Evolução da temperatura no tempo):
# Gráfico de Linha (line plot)

# Cenário B (Relação entre altura e peso): 
# Gráfico de Dispersão (scatter plot).

# Machine Learning com Scikit-learn

# Pergunta: Qual a ordem correta dos 5 passos?
# E - B - C -  A - D 

# A) Treinar o modelo com .fit() nos dados de treino.

# B) Dividir os dados em treino e teste com train_test_split().

# C) Criar uma instância do modelo (ex: modelo = DecisionTreeRegressor()).

# D) Fazer previsões com .predict() e avaliar o modelo nos dados de teste.

# E) Separar os dados em X (features) e y (target).

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor

np.random.seed(100)
dados = {
    'id_cliente': range(100),
    'idade': np.random.randint(18, 65, 100),
    'plano': np.random.choice(['Básico', 'Premium', 'Empresarial'], 100),
    'meses_como_cliente': np.random.randint(1, 48, 100),
    'satisfacao': np.random.randint(1, 6, 100) # Nota de 1 (muito insatisfeito) a 5 (muito satisfeito)
}
df_clientes = pd.DataFrame(dados)


# Sua Tarefa (em 4 partes):

# Manipulação (Módulo 1 e 2): Crie uma nova coluna chamada faixa_etaria. Se a idade do cliente for menor que 30, o valor deve ser 'Jovem'. Se for entre 30 e 50, 'Adulto'. Se for maior que 50, 'Sênior'.

def faixa_etaria(idade):
    if idade < 30:
        return 'Jovem'
    elif idade < 50:
        return 'Adulto'
    else:
        return 'Sênior'

df_clientes['faixa_etaria'] = df_clientes['idade'].apply(faixa_etaria)

print(df_clientes)

# Análise e Agrupamento (Módulo 3): Calcule a nota de satisfação média para cada tipo de plano. Qual plano tem os clientes mais satisfeitos, em média?

df_satisfacao_plano = df_clientes.groupby('plano')['satisfacao'].mean().round(2)
print("\n")
print(df_satisfacao_plano)

# Visualização (Módulo 5 - Seaborn): Crie um boxplot para visualizar a distribuição da satisfacao para cada plano. Isso ajuda a confirmar visualmente o resultado da sua análise anterior.

import matplotlib.pyplot as plt
import seaborn as sns

sns.boxplot(data=df_clientes, x='plano', y='satisfacao')
plt.show()

# Machine Learning (Módulo 5 - sklearn):
# a) Prepare os dados: Crie X (com 'idade', 'plano', 'meses_como_cliente') e y (com 'satisfacao').

# Converter a coluna 'plano' em colunas numéricas 
df_para_ml = pd.get_dummies(df_clientes, columns=['plano'], dtype=int)

#removendo as coluinas que não são features ou o proprio target
X = df_para_ml.drop(columns=['id_cliente', 'satisfacao', 'faixa_etaria'])
y = df_para_ml['satisfacao']


# b) Siga o fluxo de 5 passos para treinar um modelo para prever a satisfacao de um cliente.

X_treino, X_teste, y_treino, y_teste = train_test_split(X, y, test_size=0.3, random_state=42)

modelo_arvore = DecisionTreeRegressor(random_state=42)
modelo_arvore.fit(X_treino, y_treino)

score_r2 = modelo_arvore.score(X_teste, y_teste)
print(f"c) O Score R² do modelo de Árvore de Decisão é: {score_r2:.2f}")
print("(Um valor próximo de 0 indica que o modelo não conseguiu aprender um padrão claro, o que é esperado com dados aleatórios).")

# c) Qual o score R² do seu modelo no conjunto de teste?
