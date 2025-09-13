# Modelo -> combustivel de um motor de alta performance
# Pré-processamento é o processo de refinar e padronizar o combustivel, com o objetivo de atingir um bom desempenho.


# Problemas do mundo real
# Escalas diferentes: Uma coluna salario (3.000 a 10.000), numero_de_filhos (0 a 5). 
# Dados categóricos: Modelos de Machine learning só entendem números. 
# Ex.: 'Pais': [Brasil, Argentina], Plano: ['Básico','Premium']

# Números na mesma Escala (scaling)
#  Padronização (Standardization).
# Ferramenta: StandardScaler do Scikit-learn.
# O que faz: Média de 0 e um desvio padrão de 1 para cada coluna númerica.

from sklearn.preprocessing import StandardScaler

# 1. Crie o "padronizador"
scaler = StandardScaler()

# 2. APRENDA a escala com os dados de TREINO e os transforme
# X_treino_scaled = scaler.fit_transform(X_treino)

# X_teste_scaled = scaler.transform(X_teste)

# Texto em Números (Encoding)
# One-Hot Encoding
# Ferramenta: pd.get_dummies() 
# O que faz: Transforma as colunas categoricas em novas colunas "binárias" (0 ou 1).

import pandas as pd

df = pd.DataFrame({'Plano': ['Básico','Premium', 'Básico']})

# One-Hot
df_encoded = pd.get_dummies(df, columns=['Plano'], dtype=int)

print(df_encoded)