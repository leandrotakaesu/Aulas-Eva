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