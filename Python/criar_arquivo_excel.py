
import pandas as pd

print("Preparando os dados para cada aba...")

df_resumo = pd.DataFrame({
    'Info': ['Relatório Geral da Empresa', 'Dados confidenciais', 'Atualizado em: 29/07/2025']
})

dados_vendas = {
    'Vendedor': ['Ana', 'Bruno', 'Carlos', 'Daniela', 'Ana', 'Bruno', 'Carlos', 'Daniela'],
    'Regiao': ['Sudeste', 'Sul', 'Sudeste', 'Nordeste', 'Sul', 'Sudeste', 'Sul', 'Nordeste'],
    'Valor_Venda': [5200, 4800, 6100, 4500, 5100, 5900, 4900, 4700]
}

df_vendas_q3 = pd.DataFrame(dados_vendas)

dados_rh = {
    'ID_Funcionario': [101, 102, 103, 104],
    'Nome_Funcionario': ['Ana', 'Bruno', 'Carlos', 'Daniela'],
    'Cargo': ['Gerente', 'Vendedor', 'Vendedor', 'Vendedor']
}
df_rh = pd.DataFrame(dados_rh)


# ExcelWriter
#'with'

try:
    with pd.ExcelWriter('dados_empresa.xlsx') as writer:
        print("\nSalvando a aba 'Resumo'...")
        df_resumo.to_excel(writer, sheet_name='Resumo', index=False)
       

        print("\nSalvando a aba 'Vendas_Q3'...")
        df_vendas_q3.to_excel(writer, sheet_name='Vendas_Q3', index=False)
    
        print("\nSalvando a aba 'RH'...")
        df_rh.to_excel(writer, sheet_name='RH', index=False)

    print("\n✅ Arquivo 'dados_empresa.xlsx' criado com sucesso!")
    print("Ele está na mesma pasta onde você executou este script.")

except Exception as e:
    print(f"\n❌ Ocorreu um erro ao criar o arquivo: {e}")
    print("Verifique se você tem a biblioteca 'openpyxl' instalada (pip install openpyxl).")
