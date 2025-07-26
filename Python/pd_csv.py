# CSV significa "Comma-Separated Values" 

#a) Lendo um arquivo CSV: pd.read_csv()
# df = pd.read_csv('caminho/para/seu/arquivo.csv')

# sep(separador) - o caractere para separar as colunas
#df = pd.read_csv('arquivo.csv', sep=';')

# decimal - separar casas decimais
#df = pd.read_csv('arquivo.csv', sep=';', decimal=',')

# encoding - a codificação de caracteres do arquivo.
#df = pd.read_csv('arquivo.csv', encoding='latin-1')

#b) Salvar arquivo CSV (df.to_csv())
#df_resultado.to_csv('novo_arquivo_resultado.csv')

#index=False
#df_resultado.to_csv('resultado.csv', index=False)

import pandas as pd

df_original = pd.DataFrame({
    'Nome': ['Ana', 'Bruno'],
    'Pontuação': [9.5, 8.0]
})

df_original.to_csv('pontuacoes.csv', index=False, sep=';')
print("Arquivo salvo!")

print("\nLendo o arquivo 'pontuacoes.csv' de volta...")
df_lido = pd.read_csv('pontuacoes.csv', sep=';')

print("DataFrame lido do arquivo:")
print(df_lido)
