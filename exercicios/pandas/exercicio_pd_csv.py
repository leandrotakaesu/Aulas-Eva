# Relatório de vendas gerado em 26/07/2025
# Filial: Centro
# Produto;Quantidade_Vendida;Valor_Unitario
# Caneta;50;1,50
# Caderno;20;15,99
# Borracha;100;0,75
# Tarefa: Leia este arquivo corretamente em um DataFrame chamado df_relatorio. O DataFrame final deve ter as colunas corretas e os números (Quantidade_Vendida e Valor_Unitario) devem ser tratados como números, não como texto.

import pandas as pd

df_relatorio = pd.DataFrame({
    "Produto": ["Caneta", "Caderno", "Borracha"],
    "Quantidade_Vendida": [ 50, 20, 100],
    "Valor Unitário": [1.50, 15.99, 0.75]
})

print(df_relatorio)

df_relatorio.to_csv("Relatório_Vendas.csv", index = False, sep = ";")

# Lendo, Filtrando e Salvando um Novo CSV
# Contexto: Você recebeu um arquivo grande com dados de logs (logs_acesso.csv), mas você só precisa de algumas colunas para o seu relatório.

# Conteúdo do arquivo logs_acesso.csv:

# timestamp,ip_address,user_id,page_visited,status_code
# 2025-07-26T09:30:00,192.168.1.5,101,/home,200
# 2025-07-26T09:31:15,200.20.15.3,205,/products,200
# 2025-07-26T09:32:01,192.168.1.5,101,/cart,200
# 2025-07-26T09:33:40,187.15.2.99,312,/checkout,500

df_logs = pd.DataFrame({
    "timestamp": ["2025-07-26T09:30:00", "2025-07-26T09:31:15", "2025-07-26T09:32:01", "2025-07-26T09:33:40"],
    "ip_address": [ "192.168.1.5", "200.20.15.3", "192.168.1.5", "187.15.2.99"],
    "user_id": [101, 205, 101, 312],
    "page_visited": ["/home", "/products", "/cart", "/checkout"],
    "status_code": [200, 200, 200, 500]
})

print("\n")
print(df_logs)
df_logs.to_csv("logs_acesso.csv", index = False, sep = ";")

# Tarefas:
# a) Escreva o comando para ler o arquivo logs_acesso.csv para um DataFrame df_logs.

df = pd.read_csv("logs_acesso.csv")

# b) Crie um novo DataFrame, df_relatorio_acessos, que contenha apenas as colunas timestamp e user_id do df_logs.

df_relatorio_acessos = df_logs[["timestamp", "user_id"]]
print("\n")
print(df_relatorio_acessos)

# c) Salve o novo DataFrame df_relatorio_acessos em um arquivo chamado acessos_usuarios.csv. Garanta que o índice do DataFrame não seja salvo no arquivo.

df_relatorio_acessos.to_csv("acessos_usuarios.csv", index = False, sep = ";")