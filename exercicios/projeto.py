# ### **- Mini-Análise de Vendas**

# # Neste projeto, você será o analista de dados de uma livraria online e receberá um conjunto de dados brutos de vendas. 
# # Sua tarefa é limpar, analisar e visualizar esses dados para extrair insights valiosos.

# #### **Contexto**

# # Você recebeu os dados de vendas do último trimestre em um formato CSV "sujo". 
# # Você precisa responder a algumas perguntas da gerência sobre o desempenho de vendas.

# ### **Projeto: Análise de Vendas da Livraria Online**

# #### **Passo 0: Os Dados Brutos**

# # Os dados estão no formato de uma string CSV. Para carregá-los no pandas, você pode usar o seguinte código:


# import pandas as pd
# import io

# # Dados brutos em formato de texto (simulando um arquivo CSV)
# dados_csv = """Data_Venda,Livro,Autor,Genero,Preco,Quantidade_Vendida
# 2025-01-15,A Sombra do Vento,Carlos Ruiz Zafón,Ficção,R$ 45,50,2
# 2025-01-18,O Hobbit,J.R.R. Tolkien,Fantasia,R$ 38,90,3
# 2025-01-25,Neuromancer,William Gibson,Ficção Científica,R$ 41,20,1
# 2025-02-02,O Hobbit,J.R.R. Tolkien,Fantasia,R$ 38,90,1
# 2025-02-10,A Sombra do Vento,Carlos Ruiz Zafón,,R$ 45,50,3
# 2025-02-15,1984,George Orwell,Ficção,R$ 35,00,2
# 2025-03-05,Neuromancer,William Gibson,Ficção Científica,R$ 41,20,2
# 2025-03-12,Duna,Frank Herbert,Ficção Científica,R$ 55,00,1
# 2025-03-22,O Hobbit,J.R.R. Tolkien,Fantasia,R$ 39,90,2
# 2025-03-28,A Sombra do Vento,Carlos Ruiz Zafón,Ficção,,1
# """

# df = pd.read_csv(io.StringIO(dados_csv))


# #### **Suas Tarefas**

# **1. Inspeção e Limpeza de Dados**
# a) Inspecione o DataFrame. Verifique os tipos de dados  e se há valores nulos.
# b) A coluna `Preco` está como texto (`object`) por causa do "R$" e da vírgula. Limpe esta coluna: remova o "R$ ", os espaços, troque a vírgula por ponto e converta o tipo para `float`.
# c) A coluna `Genero` tem um valor nulo. Preencha os valores nulos com a string 'Desconhecido'.
# d) A coluna `Quantidade_Vendida` tem um valor nulo. Preencha com o valor `1` (assumindo que pelo menos um livro foi vendido).
# e) Crie uma nova coluna chamada `Faturamento`, que seja o resultado da multiplicação de `Preco` pela `Quantidade_Vendida`.

# **2. Análise Exploratória e Agrupamento**
# Responda às seguintes perguntas:
# a) Qual foi o faturamento total por **`Autor`**?
# b) Qual foi o faturamento total por **`Genero`**?
# c) Qual livro foi o mais vendido em **quantidade**?

# **3. Análise Temporal**
# a) Converta a coluna `Data_Venda` para o formato `datetime`.
# b) Defina `Data_Venda` como o índice do DataFrame.
# c) Qual foi o **faturamento total por mês**? .

# **4. Visualização de Dados**
# a) Crie um **gráfico de barras** que mostre o faturamento total por `Genero`.
# b) Crie um **gráfico de linha** que mostre a evolução do faturamento mensal (o resultado do item 3c).
