# Desafio Final: Análise de E-commerce
# Cenário: Você é o analista de dados de uma empresa de e-commerce.
# Você recebeu três arquivos de dados brutos e separados: vendas, clientes e produtos. A gerência pediu um relatório de desempenho e um modelo preditivo.
# Seu Objetivo: Limpar, integrar, analisar, visualizar e modelar os dados para gerar os insights solicitados.

import pandas as pd
import io

# Dados de Vendas
vendas_csv = """ID_Venda,ID_Produto,ID_Cliente,Data_Venda,Quantidade,Valor_Total
1,101,1,2025-01-05,2,"R$ 1.250,50"
2,102,3,2025-01-07,1,"R$ 89,90"
3,103,2,08/01/2025,5,"R$ 45,00"
4,101,3,2025-01-12,1,"R$ 625,25"
5,104,4,15/01/2025,1,
6,102,2,2025-02-02,3,"R$ 269,70"
7,105,1,2025-02-10,1,"R$ 1.899,00"
8,103,3,21/02/2025,10,"R$ 90,00"
"""

# Dados dos Clientes
clientes_csv = """ID_Cliente,Nome_Cliente,Estado,Data_Cadastro
1,Ana Silva,sp,2022-03-10
2,Bruno Costa,RJ,2021-11-25
3,Carlos Lima, Minas Gerais ,2022-08-01
4,Daniela Souza,SP,2023-01-15
"""

# Dados dos Produtos
produtos_csv = """ID_Produto,Nome_Produto,Categoria,Custo_Unitario
101,Monitor Gamer 27",Eletrônicos,450.50
102,Mousepad Gamer, Acessórios ,25.00
103,Caixa de Som USB,acessórios,7.50
104,Cadeira de Escritório,Móveis,350.00
105,Notebook Pro,eletrônicos,1400.00
"""

# Carregando os dados
df_vendas = pd.read_csv(io.StringIO(vendas_csv))
df_clientes = pd.read_csv(io.StringIO(clientes_csv))
df_produtos = pd.read_csv(io.StringIO(produtos_csv))

# Parte 1: Limpeza e Preparação (ETL)

# DataFrame de Vendas:

# Limpe a coluna Valor_Total para que ela se torne um tipo numérico (float).

df_vendas['Valor_Total'] = df_vendas['Valor_Total'].str.replace('R$ ', '')
df_vendas['Valor_Total'] = df_vendas['Valor_Total'].str.replace('.', '')
df_vendas['Valor_Total'] = df_vendas['Valor_Total'].str.replace(',', '.')
df_vendas['Valor_Total'] = pd.to_numeric(df_vendas['Valor_Total'])

# Há um valor nulo (NaN) em Valor_Total. Decida uma estratégia para tratá-lo e justifique sua escolha.

custo_produto_104 = df_produtos.loc[df_produtos['ID_Produto'] == 104, 'Custo_Unitario'].iloc[0]
quantidade_venda_5 = df_vendas.loc[df_vendas['ID_Venda'] == 5, 'Quantidade'].iloc[0]
valor_calculado = custo_produto_104 * quantidade_venda_5
df_vendas.loc[df_vendas['ID_Venda'] == 5, 'Valor_Total'] = valor_calculado

# A coluna Data_Venda tem formatos mistos (YYYY-MM-DD e DD/MM/YYYY). Unifique toda a coluna para o tipo datetime.

df_vendas['Data_Venda'] = pd.to_datetime(df_vendas['Data_Venda'], format='mixed')
print("Tabela de vendas")
print(df_vendas)

# DataFrame de Clientes:

# Padronize a coluna Estado, removendo espaços extras e convertendo os valores para siglas de 2 letras maiúsculas (ex: ' Minas Gerais ' -> 'MG').

estado_map = {
    'sp': 'SP',
    'rj': 'RJ',
    'minas gerais': 'MG'
}
df_clientes['Estado'] = df_clientes['Estado'].str.strip().str.lower().map(estado_map).fillna(df_clientes['Estado'].str.strip().str.upper())

print("\nTabela de clientes")
print(df_clientes)

# DataFrame de Produtos:

# Padronize a coluna Categoria, removendo espaços e deixando a primeira letra de cada palavra maiúscula.

df_produtos['Categoria'] = df_produtos['Categoria'].str.strip().str.title()

print("\nTabela de produtos")
print(df_produtos)

# Parte 2: Integração e Análise (BI)

# Merge: Crie um DataFrame final df_completo juntando as três tabelas.

df_completo = pd.merge(df_vendas, df_clientes, on='ID_Cliente')
df_completo = pd.merge(df_completo, df_produtos, on='ID_Produto')

print("\nTabela completa")
print(df_completo)

# Engenharia de Features: Crie uma coluna Lucro (baseada no Valor_Total e no Custo_Unitario).

df_completo['Lucro'] = df_completo['Valor_Total'] - (df_completo['Custo_Unitario'] * df_completo['Quantidade'])

# Qual o lucro total por Estado? Crie um gráfico de barras para mostrar o resultado.

lucro_por_estado = df_completo.groupby('Estado')['Lucro'].sum().sort_values(ascending=False)

import matplotlib.pyplot as plt

lucro_por_estado.plot(kind='bar', color='skyblue')
plt.title('Lucro Total por Estado')
plt.xlabel('Estado')
plt.ylabel('Lucro Total (R$)')
plt.show()

# Como o faturamento (Valor_Total) evoluiu ao longo do tempo? Crie um gráfico de linha mostrando o faturamento total por mês.

df_completo['Mes_Venda'] = df_completo['Data_Venda'].dt.to_period('M')
faturamento_mensal = df_completo.groupby('Mes_Venda')['Valor_Total'].sum().sort_index()
faturamento_mensal.index = faturamento_mensal.index.astype(str)

faturamento_mensal.plot(kind='line', marker='o', color='green')
plt.title('Faturamento Mensal')
plt.xlabel('Mês da Venda')
plt.ylabel('Faturamento Total (R$)')
plt.show()

# Parte 3: Modelagem Preditiva (Machine Learning)
# Objetivo: Criar um modelo que preveja a Categoria de um produto com base no seu Custo_Unitario e no Lucro que ele gera.

# Preparação: Separe o df_completo em X (features) e y (target).

X = df_completo[['Custo_Unitario', 'Lucro']]
y = df_completo['Categoria']

# Pré-processamento: Padronize as features numéricas em X, pois elas têm escalas diferentes.

from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

from sklearn.preprocessing import LabelEncoder

le = LabelEncoder()
y_encoded = le.fit_transform(y)

# Treinamento: Siga o fluxo de 5 passos para treinar um modelo RandomForestClassifier.

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X_scaled, y_encoded, test_size = 0.3, random_state = 42)

from sklearn.ensemble import RandomForestClassifier

model = RandomForestClassifier(n_estimators = 100, random_state=42)
model.fit(X_train, y_train)
y_pred = model.predict(X_test)

# Avaliação: Calcule a acurácia e plote a matriz de confusão para avaliar o desempenho do seu modelo.

from sklearn.metrics import accuracy_score, confusion_matrix

accuracy = accuracy_score(y_test, y_pred)
print(f"\nAcurácia do modelo: {accuracy:.2f}")
cm = confusion_matrix(y_test, y_pred)
labels = le.inverse_transform(model.classes_) # Obtém os nomes das classes na ordem correta

import seaborn as sns

plt.figure(figsize=(8, 6))
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', xticklabels=labels, yticklabels=labels)
plt.title('Matriz de Confusão')
plt.xlabel('Previsto')
plt.ylabel('Verdadeiro')
plt.show()