# Exercícios: Datas - Conversão, Indexação e Seleção

# Contexto

# Você recebeu um registro de acessos a um site. 
# As datas estão como texto e você precisa organizá-las para fazer análises temporais.


# import pandas as pd

# dados_acessos = {
#     'data_str': ['2024-05-01', '2024-05-01', '2024-05-02', '2024-05-03', '2024-05-03', '2024-05-04'],
#     'pagina_visitada': ['/home', '/produtos', '/home', '/precos', '/produtos', '/home'],
#     'tempo_gasto_s': [120, 300, 80, 150, 240, 95]
# }

# df_acessos = pd.DataFrame(dados_acessos)


# Exercícios

# 1. Conversão para `datetime`
# a) Verifique os tipos de dados (`Dtypes`) do `df_acessos`  para confirmar que a coluna `data_str` é do tipo `object`.
# b) Crie uma nova coluna chamada `data_dt` convertendo a coluna `data_str` para o tipo `datetime`.
# c) Verifique novamente os tipos de dados  para confirmar que a nova coluna `data_dt` é do tipo `datetime64[ns]`.

# 2. Definindo um Índice de Data e Hora
# a) Crie um novo DataFrame chamado `df_acessos_idx` definindo a coluna `data_dt` como o novo índice do `df_acessos`.
# b) Exiba as primeiras linhas do `df_acessos_idx` para ver como ele ficou com o novo índice de data.

# 3. Seleção por Datas
# a) Selecione e exiba todos os acessos que ocorreram no dia **'2024-05-01'**.
# b) Selecione e exiba todos os acessos que ocorreram no intervalo de **'2024-05-02' até '2024-05-03'**.
# c) Selecione e exiba o `tempo_gasto_s` do primeiro acesso do dia **'2024-05-03'**. 



# Crie um novo DataFrame chamado `acessos_maio_inicio` que contenha apenas os acessos da primeira quinzena de maio (até o dia 15).

