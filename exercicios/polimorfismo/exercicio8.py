# ✅ Exercício 1: Sistema de Cálculo de Salário de Funcionários
# Objetivo: Modelar diferentes tipos de funcionários em uma empresa. Todos são "funcionários", mas a forma de calcular o pagamento de cada um é diferente. Uma classe abstrata é perfeita para garantir que todo funcionário saiba como "calcular seu pagamento".

# 📋 Enunciado: 

# Crie uma classe abstrata Funcionario que herda de ABC.

# No construtor (__init__), ela deve receber nome e matricula.

# Ela deve ter um método concreto chamado exibir_dados(), que imprime o nome, a matrícula e o resultado do cálculo do pagamento.

# Ela deve ter um método abstrato chamado calcular_pagamento(self), que será implementado pelas subclasses.

# Crie três classes concretas que herdam de Funcionario:

# FuncionarioFixo: Além de nome e matrícula, recebe um salario_base no construtor. O método calcular_pagamento simplesmente retorna este salário base.

# FuncionarioComissionado: Além de nome e matrícula, recebe um salario_base, uma comissao por venda e um numero_de_vendas. O calcular_pagamento deve retornar o salario_base + (comissao * numero_de_vendas).

# FuncionarioHorista: Além de nome e matrícula, recebe um valor_hora e o total_de_horas_trabalhadas. O calcular_pagamento deve retornar valor_hora * total_de_horas_trabalhadas.

from abc import ABC, abstractmethod

class Funcionario(ABC):
    def __init__(self, nome, matricula, salario_base):
        self.nome = nome
        self.matricula = matricula
        self.salario_base = salario_base

    def exibir_dados(self):
        salario = self.calcular_pagamento()
        print(f"O funcionário {self.nome}, matrícula {self.matricula}, recebe R$ {salario}")

    @abstractmethod
    def calcular_pagamento(self)->float:
        pass

class FuncionarioFixo(Funcionario):
    def __init__(self, nome, matricula, salario_base):
        super().__init__(nome, matricula, salario_base)

    def calcular_pagamento(self)->float:
        return self.salario_base
    
funcionario1 = FuncionarioFixo("João", 123, 2500)
funcionario1.exibir_dados()

class FuncionarioComissionado(Funcionario):
    def __init__(self, nome, matricula, salario_base, numero_vendas, valor_comissao):
        super().__init__(nome, matricula, salario_base)
        self.numero_vendas = numero_vendas
        self.valor_comissao = valor_comissao

    def calcular_pagamento(self)->float:
        salario = self.salario_base + self.numero_vendas * self.valor_comissao
        return salario

funcionario2 = FuncionarioComissionado("Pedro", 246, 2500, 10, 100)
funcionario2.exibir_dados()

class FuncionarioHorista(Funcionario):
    def __init__(self, nome, matricula, salario_base, valor_hora, total_horas):
        super().__init__(nome, matricula, salario_base)
        self.valor_hora = valor_hora
        self.total_horas = total_horas
    
    def calcular_pagamento(self)->float:
        salario = self.salario_base + self.valor_hora * self.total_horas
        return salario
    
funcionario3 = FuncionarioHorista("Marcos", 321, 0, 8, 200)
funcionario3.exibir_dados()