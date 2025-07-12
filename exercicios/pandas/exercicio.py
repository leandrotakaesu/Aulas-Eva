# Exercícios de Revisão: Módulo 1 - A Fundação

# #### **Contexto**

# Imagine que você recebeu uma pequena lista de dados sobre produtos de uma loja de eletrônicos e precisa organizá-la em um DataFrame para começar a análise.

# #### **Exercício 1: Criação de um DataFrame**

# a) Crie um dicionário Python com os seguintes dados:

# ```
# dados_produtos = {
#     'ID_Produto': [10, 20, 30, 40, 50],
#     'Nome_Produto': ['Teclado', 'Mouse', 'Monitor', 'Webcam', 'Headset'],
#     'Preco': [120.00, 75.50, 899.99, 250.00, 300.75],
#     'Estoque': [35, 80, 22, 15, 30]
# }
# ```

import pandas as pd

dados_produtos = {
    'ID_Produto': [10, 20, 30, 40, 50],
    'Nome_Produto': ['Teclado', 'Mouse', 'Monitor', 'Webcam', 'Headset'],
    'Preco': [120.00, 75.50, 899.99, 250.00, 300.75],
    'Estoque': [35, 80, 22, 15, 30]
}

# b) Usando o dicionário acima, crie um DataFrame do pandas chamado `df_produtos`.

df_produtos = pd.DataFrame(dados_produtos)

# c) Exiba o DataFrame completo na tela para verificar se ele foi criado corretamente.

print('DataFrame de Produtos')
print(df_produtos)

# #### **Exercício 2: Inspeção Inicial do DataFrame**

# Agora que você tem o `df_produtos`, use os comandos de inspeção para responder às seguintes perguntas. Para cada item, escreva o comando que você usaria.

# a) Como você visualizaria apenas as **3 primeiras linhas** do DataFrame?

print(df_produtos.head(3))

# b) Como você obteria um resumo técnico que mostra os tipos de dados de cada coluna e a contagem de valores não nulos?

df_produtos.info()

# c) Como você descobriria as dimensões do DataFrame (quantas linhas e colunas ele tem)?

print(df_produtos.shape)

# d) Como você visualizaria um resumo estatístico (média, desvio padrão, mínimo, máximo, etc.) para as colunas numéricas?

print(df_produtos.describe())

# e) Como você listaria apenas os nomes de todas as colunas?

print(df_produtos.columns)

# #### **Exercício 3: Seleção e Indexação de Dados**

# Use o `df_produtos` para realizar as seguintes seleções.

# a) Selecione e exiba apenas a coluna **`Nome_Produto`**.

df_produtos["Valor do estoque"] = df_produtos["Preco"] * df_produtos["Estoque"]
print(df_produtos)

# b) Selecione e exiba as colunas **`Nome_Produto`** e **`Preco`**.

print(df_produtos[["Nome_Produto", "Preco"]])

# c) Use o método `.loc` para selecionar e exibir a linha correspondente ao produto **"Monitor"**. (Dica: primeiro você precisará descobrir o índice do "Monitor" ou definir uma coluna como índice).

indice_monitor = df_produtos[df_produtos['Nome_Produto'] == 'Monitor'].index[0]
print(df_produtos.loc[indice_monitor])

#   * **Desafio extra:** Como você faria isso se definisse a coluna `ID_Produto` como o índice do DataFrame?

df_com_id_index = df_produtos.set_index('ID_Produto')
print(df_com_id_index)

# d) Use o método `.iloc` para selecionar e exibir a **última linha** do DataFrame.

print(df_produtos.iloc[-1])

# e) Use o método `.loc` para selecionar e exibir o **preço do produto na linha de índice 2**.

print(df_com_id_index.loc[30, "Preco"])
