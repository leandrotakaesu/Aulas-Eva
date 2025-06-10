import pandas

# "nome" → lista com 3 nomes.

# "idade" → lista com as idades dessas pessoas.

# "salario" → lista com os salários respectivos.
dados = {
    "nome": ["Ana", "Bruno", "Carlos"],
    "idade": [25,35,29],
    "salario": [3000, 4500, 3800],
    "setor": ["TI", "Marketing", "RH"],
    "cidade": ["São Paulo", "Campinas", "Santos"]
}

df = pandas.DataFrame(dados) #transforma o dicionário num dataframe

print(df)

print(df["salario"]) # imprime a coluna desejada

print(df.iloc[2]) #imprime a linha desejada

df = df.set_index("nome")
#print(df.loc["Ana"])

maisde30 = df[df["idade"] > 30] #df["idade"] > 30 retorna uma série booleana (True/False). o que equivale a um if
#df[...] filtra o DataFrame com base nessas condições.

print(maisde30)