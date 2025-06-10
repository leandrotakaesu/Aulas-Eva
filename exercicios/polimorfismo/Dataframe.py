import pandas as pd

dados = {
    "id": [201, 202, 203, 204, 205],
    "nome": ["Eva", "Fábio", "Gustavo", "Helena", "Igor"],
    "idade": [27, 32, 29, 41, 36],
    "salario": [4100, 5200, 3900, 5800, 4700],
    "setor": ["TI", "RH", "TI", "Financeiro", "RH"]
}

df = pd.DataFrame(dados)

# print(df.iloc[2])

# print(df[["nome", "salario"]])

# print(df[df["setor"] == "RH"])

# df["salario anual"] = df["salario"] * 12

# print(df)

# print(df["idade"].mean())

maior_salario = df["salario"].idxmax()
funcionario_maior_salario = df.iloc[maior_salario]
print(funcionario_maior_salario[["nome", "salario"]])

df = df.set_index(["id"])

print(df.loc[204])

df.loc[202, "setor"] = "administrativo"

df["nivel"] = None

print(df)

def nivel(salario):
    if salario >= 5000:
        return "senior" 
    elif salario > 4000:
        return "pleno"
    return "junior"
    
df["nivel"] = df["salario"].apply(nivel)

print(df)

import numpy as np

# Defina as condições e as escolhas correspondentes
conditions = [
    df['salario'] > 5000,
    df['salario'] >= 4000
]
choices = ['Sênior', 'Pleno']

# Crie a coluna 'nivel' usando np.select
# O 'default' é o valor se nenhuma condição for atendida (equivalente ao 'else')
df['nivel'] = np.select(conditions, choices, default='Júnior')

print(df)