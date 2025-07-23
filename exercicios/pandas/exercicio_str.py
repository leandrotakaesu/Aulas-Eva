# # Exercícios: Módulo  Manipulação de Strings com `.str`

# # Contexto

# # Você recebeu uma lista de novos funcionários e precisa limpar e padronizar as informações para inseri-las no sistema da empresa.

# import pandas as pd

# dados_funcionarios = {
#     'ID_Funcionario': [' a-101 ', 'b-202', ' C-303', 'd-404 '],
#     'Nome_Completo': ['Ana silva', ' BRUNO COSTA', 'Carlos de souza', 'DANIELA oliveira'],
#     'Email': ['ana.silva@empresa.com', 'bruno@gmail.com', 'carlos.souza@EMPRESA.COM', 'daniela@hotmail.com'],
#     'Cargo': ['Analista de Dados Pleno', 'Engenheiro de Software Sênior', 'Gerente de Projetos', 'Analista de Dados Júnior']
# }
# df_func = pd.DataFrame(dados_funcionarios)

#  Exercícios

# 1. Limpeza e Padronização de Dados
# a) Crie uma nova coluna `ID_Limpo` que seja a coluna `ID_Funcionario` sem espaços em branco no início ou no fim, e com todo o texto em letras maiúsculas.
# b) Padronize a coluna `Nome_Completo` para que todos os nomes comecem com a primeira letra de cada palavra maiúscula e o resto seja minúsculo.
# c) Padronize a coluna `Email` para que todos fiquem em letras minúsculas.

# 2. Filtragem por Padrões de Texto
# a) Crie um novo DataFrame `df_empresa` que contenha apenas os funcionários com e-mail corporativo (que termina com `@empresa.com`). A verificação não deve ser sensível a maiúsculas/minúsculas.
# b) Crie um novo DataFrame `df_analistas` que contenha apenas os funcionários cujo cargo contenha a palavra "Analista".

# 3. Extração de Informações com `.str.split()`
# a) A partir da coluna `ID_Limpo` (criada no exercício 1), crie duas novas colunas no `df_func`: `Letra_ID` e `Numero_ID`, contendo as partes separadas do ID.
# b) A partir da coluna `Nome_Completo` (já padronizada no exercício 1), crie uma nova coluna `Primeiro_Nome`, contendo apenas a primeira parte do nome.


#  Desafio

# Extraia o nível de senioridade de cada funcionário a partir da coluna `Cargo` e conte quantos funcionários existem em cada nível.

# Passos:

# 1.  Crie uma nova coluna chamada `Nivel_Senioridade`.
# 2.  Para cada linha, verifique se a coluna `Cargo` contém 'Júnior', 'Pleno' ou 'Sênior'. O valor da nova coluna deve ser a palavra encontrada.
# 3.  Se nenhuma dessas palavras for encontrada, o valor deve ser 'Não especificado'.
# 4.  Depois de criar a coluna, use `.value_counts()` para contar quantos funcionários há em cada nível.
