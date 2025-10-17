# Conceito: Herança

# O que é: Uma classe filha que herda todas as características e ações de uma classe mãe, podendo adicionar as suas próprias especializações.

# Seu Exemplo (de Classe.py): Você criou uma classe Gerente que é um tipo de Funcionario. Ela herda nome e salario, mas adiciona o seu próprio atributo setor.

# Python

# class Funcionario:
#     def __init__(self, nome, salario):
#         self.nome = nome
#         self.salario = salario
#     def info(self):
#          return f"{self.nome} ganha R$ {self.salario: 2f}"

# class Gerente(Funcionario): # Gerente herda de Funcionario
#     def __init__(self, nome, salario, setor):
#         super().__init__(nome, salario) # Chama o construtor da classe mãe
#         self.setor = setor