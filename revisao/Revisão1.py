import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor

# --- DADOS ---
np.random.seed(100)
dados = {
    'id_cliente': range(100),
    'idade': np.random.randint(18, 65, 100),
    'plano': np.random.choice(['Básico', 'Premium', 'Empresarial'], 100),
    'meses_como_cliente': np.random.randint(1, 48, 100),
    'satisfacao': np.random.randint(1, 6, 100)
}
df_clientes = pd.DataFrame(dados)


print("--- 1. Manipulação: Criando a coluna 'faixa_etaria' ---")
# Função para aplicar a lógica
def classificar_faixa_etaria(idade):
    if idade < 30:
        return 'Jovem'
    elif 30 <= idade <= 50:
        return 'Adulto'
    else:
        return 'Sênior'

# Aplicando a função para criar a nova coluna
df_clientes['faixa_etaria'] = df_clientes['idade'].apply(classificar_faixa_etaria)
print("DataFrame com a nova coluna (5 primeiras linhas):")
print(df_clientes.head())


print("\n--- 2. Análise e Agrupamento: Satisfação Média por Plano ---")
satisfacao_media_plano = df_clientes.groupby('plano')['satisfacao'].mean().round(2)
print(satisfacao_media_plano)


print("\n--- 3. Visualização: Boxplot da Satisfação por Plano ---")
plt.figure(figsize=(10, 6))
sns.boxplot(data=df_clientes, x='plano', y='satisfacao')
plt.title('Distribuição da Satisfação do Cliente por Plano')
plt.show()