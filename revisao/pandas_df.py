import pandas

dados = {
    "nome": ["Ana", "Bruno", "Carlos"],
    "idade": [25,35,29],
    "salario": [3000, 4500, 3800],
    "endereco": ['3000', '4500', '3800']
}
df = pandas.DataFrame(dados) # Transforma o dicionário num dataframe
# print(df)

# Para ver as 5 primeiras linhas e ter uma amostra visual.
df.head()

# Para verificar os tipos de dados de cada coluna (se números são int ou float, se texto é object) e contar valores não nulos
df.info()

# Para obter estatísticas rápidas (média, mediana, mínimo, máximo) das colunas numéricas.
df.describe()

# Para saber quantas linhas e colunas a tabela possui.
df.shape

# Leitura e escrita de arquivos
# Como carregar dados de fontes externas (CSV, Excel) para um DataFrame e como salvar seus resultados.


# Exemplo de Leitura CSV (de pd_csv.py): Você leu um arquivo pontuacoes.csv, especificando o separador como ponto e vírgula (sep=';').
# df_lido = pd.read_csv('pontuacoes.csv', sep=';')

# Exemplo de Escrita CSV (de pd_csv.py): Você salvou um DataFrame, garantindo que o índice não fosse incluído (index=False) e usando o separador correto.
# df_original.to_csv('pontuacoes.csv', index=False, sep=';')

# Exemplo de Leitura Excel (de pd_xlsx.py): O conceito de ler uma aba específica com sheet_name foi explicado.
# Conceito: Ler apenas a aba 'Vendas_2025'
# df = pd.read_excel('planilha.xlsx', sheet_name='Vendas_2025')

# Exemplo de Escrita Excel Multi-abas (de criar_arquivo_excel.py): Você usou o ExcelWriter para salvar múltiplos DataFrames em diferentes abas ('Resumo', 'Vendas_Q3', 'RH') dentro do mesmo arquivo .xlsx
# with pd.ExcelWriter('dados_empresa.xlsx') as writer:
#     df_resumo.to_excel(writer, sheet_name='Resumo', index=False)
#     df_vendas_q3.to_excel(writer, sheet_name='Vendas_Q3', index=False)
#     df_rh.to_excel(writer, sheet_name='RH', index=False)


# 3. Limpeza de Dados com .str

# Conceito: Utilizar o acessor .str para aplicar funções de manipulação de texto em colunas inteiras do DataFrame. Essencial para padronização.

# Exemplo (de str.py): Você limpou a coluna sku removendo espaços (.strip()) e convertendo para maiúsculas (.upper()), e a coluna produto_desc removendo espaços e capitalizando (.capitalize()).

# Exemplo Avançado (de exercicio_str.py): Você usou .str.split() com expand=True para dividir a coluna ID_Funcionario em duas novas colunas (Letra_ID e Numero_ID) com base no delimitador -.

# df_func[["Letra_ID", "Numero_ID"]] = df_func["ID_Funcionario"].str.split("-", expand = True)

# 4. Combinação de Dados (concat e merge)

# Conceito: Unir informações de diferentes DataFrames. concat empilha tabelas com a mesma estrutura, enquanto merge junta tabelas lateralmente com base em colunas-chave.

# Exemplo concat (de exercicio_concat.py): Você combinou as vendas de df_loja_a e df_loja_b em um único DataFrame df_vendas_total, usando ignore_index=True para resetar os índices.



# df_vendas_total = pd.concat([df_loja_a, df_loja_b], ignore_index = True)
# Exemplo merge (de merge.py): Você explorou os diferentes tipos de join (inner, left, right, outer) para juntar df_vendas e df_produtos pela coluna id_produto, vendo como cada how afeta o resultado final.



# # Exemplo de left join: mantém todas as vendas, mesmo se o produto não existir
# df_left = pd.merge(df_vendas, df_produtos, on='id_produto', how='left')
# 5. Agregação e Agrupamento (groupby, agg, pivot_table)

# Conceito: Ferramentas fundamentais para resumir dados e responder perguntas de negócio. groupby agrupa linhas por categorias, agg permite aplicar múltiplas funções de agregação, e pivot_table reorganiza os dados numa matriz.

# Exemplo groupby Simples (de exercicios_agregacao.py): Calculou o preço médio por Categoria.



# preco_medio_categoria = df_vendas.groupby("Categoria")["Preço"].mean()
# Exemplo groupby com agg (de exercicios_agregacao.py): Calculou a contagem (count) e a soma (sum) das vendas por Forma_Pagamento numa única operação.



# vendas_forma_pagamento = df_vendas.groupby("Forma_Pagamento").agg({"Preço": ["count", "sum"]})
# Exemplo pivot_table (de tabela_pivo.py): Reorganizou os dados para mostrar o valor total de vendas (sum) para cada Categoria (colunas) dentro de cada Cidade (linhas).



# tabela_pivo = df_vendas.pivot_table(
#     index='Cidade',
#     columns='Categoria',
#     values='ValorVenda',
#     aggfunc='sum',
#     fill_value=0
# )