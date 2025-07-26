# Exercícios: Lendo e Salvando Arquivos (I/O)
# Exercício 1: Lendo um CSV "brasileiro"
# Contexto: Você recebeu um arquivo de relatório de vendas (relatorio.csv) que foi gerado por um sistema antigo. Ele usa ponto e vírgula (;) como separador e vírgula (,) como separador decimal. Além disso, as primeiras linhas são comentários.

# Conteúdo do arquivo relatorio.csv:

# Relatório de vendas gerado em 26/07/2025
# Filial: Centro
# Produto;Quantidade_Vendida;Valor_Unitario
# Caneta;50;1,50
# Caderno;20;15,99
# Borracha;100;0,75
# Tarefa: Leia este arquivo corretamente em um DataFrame chamado df_relatorio. O DataFrame final deve ter as colunas corretas e os números (Quantidade_Vendida e Valor_Unitario) devem ser tratados como números, não como texto.

# Exercício 2: Lendo, Filtrando e Salvando um Novo CSV
# Contexto: Você recebeu um arquivo grande com dados de logs (logs_acesso.csv), mas você só precisa de algumas colunas para o seu relatório.

# Conteúdo do arquivo logs_acesso.csv:

# timestamp,ip_address,user_id,page_visited,status_code
# 2025-07-26T09:30:00,192.168.1.5,101,/home,200
# 2025-07-26T09:31:15,200.20.15.3,205,/products,200
# 2025-07-26T09:32:01,192.168.1.5,101,/cart,200
# 2025-07-26T09:33:40,187.15.2.99,312,/checkout,500
# Tarefas:
# a) Escreva o comando para ler o arquivo logs_acesso.csv para um DataFrame df_logs.
# b) Crie um novo DataFrame, df_relatorio_acessos, que contenha apenas as colunas timestamp e user_id do df_logs.
# c) Salve o novo DataFrame df_relatorio_acessos em um arquivo chamado acessos_usuarios.csv. Garanta que o índice do DataFrame não seja salvo no arquivo.
