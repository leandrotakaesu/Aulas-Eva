import pandas as pd

df = pd.DataFrame({'Data': ['2025-07-18', '2025-07-19'], 'Vendas': [100, 150]})
df.info() # -> Dtype da coluna 'Data' será 'object'

df['Data'] = pd.to_datetime(df['Data'])
df.info() 

dados = {
    'Data': pd.to_datetime(['2025-07-15', '2025-07-15', '2025-07-16', '2025-07-16', '2025-07-17', '2025-07-17', '2025-07-18', '2025-07-18']),
    'Vendedor': ['Ana', 'Bruno', 'Ana', 'Carlos', 'Bruno', 'Ana', 'Carlos', 'Bruno'],
    'Regiao': ['Sudeste', 'Sul', 'Sudeste', 'Sudeste', 'Sul', 'Nordeste', 'Sudeste', 'Nordeste'],
    'Produto': ['Desktop', 'Laptop', 'Desktop', 'Laptop', 'Desktop', 'Laptop', 'Desktop', 'Laptop'],
    'Valor': [3000, 5000, 3200, 4800, 3100, 5500, 2900, 5200]
}
df_vendas = pd.DataFrame(dados)

df_vendas_temporal = df_vendas.set_index('Data')
print(df_vendas_temporal)

#             Vendedor     Regiao  Produto  Valor
# Data                                           
# 2025-07-15       Ana    Sudeste  Desktop   3000
# 2025-07-15     Bruno        Sul   Laptop   5000
# 2025-07-16       Ana    Sudeste  Desktop   3200

# Selecionar todas as vendas de um dia específico
vendas_dia_16 = df_vendas_temporal.loc['2025-07-16':'2025-07-18']
print(vendas_dia_16)
df_vendas.info()
df_vendas_temporal.info()
#  Selecionar um intervalo de datas

df_vendas_temporal['Dia_Semana'] = df_vendas_temporal.index.day_name()
print(df_vendas_temporal)