import pandas as pd

dados_funcionarios = {
  "ID_Funcionario": [" a-101 ", "b-202", " C-303", "d-404 "],
  "Nome_Completo": ["Ana silva", " BRUNO COSTA", "Carlos de souza", "DANIELA oliveira"],
  "Email": ["ana.silva@empresa.com", "bruno@gmail.com", "carlos.souza@EMPRESA.COM", "daniela@hotmail.com"],
  "Cargo": ["Analista de Dados Pleno", "Engenheiro de Software Sênior", "Gerente de Projetos", "Analista de Dados Júnior"]
}
df_func = pd.DataFrame(dados_funcionarios)

# 1. Limpeza e Padronização de Dados
# a) Crie uma nova coluna `ID_Limpo` que seja a coluna `ID_Funcionario` sem espaços em branco no início ou no fim, e com todo o texto em letras maiúsculas.

df_func["ID_Funcionario"] = df_func["ID_Funcionario"].str.strip().str.upper()

# b) Padronize a coluna `Nome_Completo` para que todos os nomes comecem com a primeira letra de cada palavra maiúscula e o resto seja minúsculo.

df_func["Nome_Completo"] = df_func["Nome_Completo"].str.strip().str.title()

# c) Padronize a coluna `Email` para que todos fiquem em letras minúsculas.

df_func["Email"] = df_func["Email"].str.strip().str.lower()
print(df_func)

# 2. Filtragem por Padrões de Texto
# a) Crie um novo DataFrame `df_empresa` que contenha apenas os funcionários com e-mail corporativo (que termina com `@empresa.com`). A verificação não deve ser sensível a maiúsculas/minúsculas.

df_empresa = df_func[df_func["Email"].str.endswith("@empresa.com")]
print("\n")
print(df_empresa)

# b) Crie um novo DataFrame `df_analistas` que contenha apenas os funcionários cujo cargo contenha a palavra "Analista".

df_analistas = df_func[df_func["Cargo"].str.contains("Analista")]
print("\n")
print(df_analistas)

# 3. Extração de Informações com `.str.split()`
# a) A partir da coluna `ID_Limpo` (criada no exercício 1), crie duas novas colunas no `df_func`: `Letra_ID` e `Numero_ID`, contendo as partes separadas do ID.

df_func["Letra_ID"] = df_func["ID_Funcionario"].str.split("-", expand = True)[0]
df_func["Numero_ID"] = df_func["ID_Funcionario"].str.split("-", expand = True)[1]
print("\n")
print(df_func)

# b) A partir da coluna `Nome_Completo` (já padronizada no exercício 1), crie uma nova coluna `Primeiro_Nome`, contendo apenas a primeira parte do nome.

df_func["Primeiro_Nome"] = df_func["Nome_Completo"].str.split(" ", expand = True)[0]
print("\n")
print(df_func)

# Desafio
# Extraia o nível de senioridade de cada funcionário a partir da coluna `Cargo` e conte quantos funcionários existem em cada nível.
# 1. Crie uma nova coluna chamada `Nivel_Senioridade`.
# 2. Para cada linha, verifique se a coluna `Cargo` contém 'Júnior', 'Pleno' ou 'Sênior'. O valor da nova coluna deve ser a palavra encontrada.
# 3. Se nenhuma dessas palavras for encontrada, o valor deve ser 'Não especificado'.
# 4. Depois de criar a coluna, use `.value_counts()` para contar quantos funcionários há em cada nível.

def extrair_nivel_senioridade(cargo):
  if "Júnior" in cargo:
    return "Júnior"
  elif "Pleno" in cargo:
    return "Pleno"
  elif "Sênior" in cargo:
    return "Sênior"
  else:
    return "Não especificado"
  
df_func["Nível_Senioridade"] = df_func["Cargo"].apply(extrair_nivel_senioridade)
print("\n")
print(df_func)

df_nivel_senioridade = df_func["Nível_Senioridade"].value_counts()
print("\n")
print(df_nivel_senioridade)