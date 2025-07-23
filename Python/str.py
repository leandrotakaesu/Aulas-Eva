import pandas as pd

dados = {
    'produto_desc': ['  Notebook Dell  ', 'TECLADO mecânico', 'mouse sem fio logitech', 'MONITOR 4K SAMSUNG '],
    'sku': [' SKU-001-ELE ', 'sku-002-ace', '  sku-003-ace', 'SKU-004-ELE']
}
df = pd.DataFrame(dados)
print("DataFrame Original:")
print(df)

# Metodos de limpeza
# .str.strip(): Remover os espacos em branco do inicio e fim
# .str.lower(): Converter todo o texto em letra minuscula
# .str.upper(): Converter todo o texto em letra maiuscula
# .str.replace('antigo', 'novo'): Substitui parte do texto por outra


# Limpando a coluna 'sku'
df['sku_limpo'] = df['sku'].str.strip().str.upper()

# Limpando a coluna 'produto_desc'
df['produto_limpo'] = df['produto_desc'].str.strip().str.capitalize()

print("\nDataFrame Após Limpeza:")
print(df)

# Filtragem
# .str.contains('texto'): Verifica se o texto contém uma substring.

# .str.startswith('prefixo'): Verifica se o texto começa com um prefixo.

# .str.endswith('sufixo'): Verifica se o texto termina com um sufixo.

monitores = df[df['produto_limpo'].str.contains('Monitor')]
print("\nFiltrando por 'Monitor':")
print(monitores)


# Divisão e Extração de Informações
# .str.split('delimitador'): Quebra o texto em uma lista, usando um delimitador.

# .str.split('delimitador', expand=True): Faz o mesmo, mas já cria novas colunas com os resultados da quebra.

# Quebrando a coluna 'sku_limpo' em 3 novas colunas
df[['Tipo', 'Codigo', 'Categoria_SKU']] = df['sku_limpo'].str.split('-', expand=True)

print("\nDataFrame com colunas extraídas do SKU:")
print(df)