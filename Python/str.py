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


