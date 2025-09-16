# One Hot Encoding ou criação de variavéis dummy

# Converter dados categoricos (texto) em um formato numerico 
# Com o objetivo de os algortimos de machine learning conseguirem entender e processar.

# presença - 1
# ausencia - 0
import pandas as pd

dados = {'cliente_id': [101, 102, 103, 104],
         'plano': ['Básico', 'Premium', 'Premium', 'Básico']}
df = pd.DataFrame(dados)

print("DataFrame Original:")
print(df)

df_transformado = pd.get_dummies(df, columns=['plano'], prefix="tipo_plano")

print("\nDataFrame Transformado:")
print(df_transformado)
