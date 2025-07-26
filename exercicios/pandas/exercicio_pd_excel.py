
# Exercício 3: Lendo uma Aba Específica de um Arquivo Excel
# Contexto: Você recebeu um arquivo Excel (dados_empresa.xlsx) com várias abas, mas os dados que você precisa estão em uma aba chamada "Vendas_Q3".

# Descrição do arquivo dados_empresa.xlsx:

# Aba 1 (nome Resumo): Contém gráficos e texto.

# Aba 2 (nome Vendas_Q3): Contém uma tabela com as colunas Vendedor, Regiao, Valor_Venda.

# Aba 3 (nome RH): Contém dados de funcionários.

# Tarefa: Escreva o comando pd.read_excel() para ler apenas a aba Vendas_Q3 e carregar seus dados em um DataFrame chamado df_vendas_q3.

# Desafio: Lendo, Processando e Salvando em Múltiplas Abas do Excel
# Contexto: Usando o df_vendas_q3 do exercício anterior, seu chefe pediu para você separar as vendas por região e salvar em um novo arquivo Excel, com cada região em sua própria aba.

# Tarefas:
# a) A partir do df_vendas_q3 (imagine que ele já foi carregado), crie dois novos DataFrames: df_sudeste (filtrando apenas as vendas da Região 'Sudeste') e df_sul (filtrando apenas as vendas da Região 'Sul').
# b) Escreva o código para salvar esses dois DataFrames (df_sudeste e df_sul) em um único novo arquivo Excel chamado relatorio_regioes.xlsx.
# * df_sudeste deve ser salvo em uma aba chamada "Vendas Sudeste".
# * df_sul deve ser salvo em uma aba chamada "Vendas Sul".
# * O índice não deve ser salvo em nenhuma das abas.


# with pd.ExcelWriter('nome_do_arquivo.xlsx') as writer:
#     df1.to_excel(writer, sheet_name='Nome_Aba_1', index=False)
#     df2.to_excel(writer, sheet_name='Nome_Aba_2', index=False)