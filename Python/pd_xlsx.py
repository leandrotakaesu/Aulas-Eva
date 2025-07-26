#Arquivos Excel (.xlsx)
#Necessario instalar a biblioteca abaixo:
#python -m pip install openpyxl

#a) Lendo um arquivo Excel: pd.read_excel()

#df = pd.read_excel('caminho/para/seu/arquivo.xlsx')

#sheet_name: Especifica qual a aba (planilha) nome ou o numero(comecando em 0)
#df = pd.read_excel('planilha.xlsx', sheet_name='Vendas_2025')

# b) Salvando em um arquivo Excel: df.to_excel()
#df_resultado.to_excel('relatorio_final.xlsx', index=False)
