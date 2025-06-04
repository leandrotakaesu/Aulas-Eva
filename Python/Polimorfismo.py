class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    
    def getNome(self):
        return self.nome
    
    def setNome(self, nome):
        self.nome = nome

    def getIdade(self):
        return self.nome
    
    def setIdade(self, idade):
        self.idade = idade

    def info(self):
        return f"{self.nome}, {self.idade} anos"


class Aluno(Pessoa):
    def __init__(self, nome, idade, curso):
        super().__init__(nome,idade)
        self.curso = curso


    def info(self):
        return f"{super().getNome()}, cursando {self.curso}"

class Professor(Pessoa):
    def __init__(self, nome, idade, salario):
        super().__init__(nome,idade)
        self.salario = salario

    def info(self):
        return f"{super().info()}, salario R$ {self.salario}"

aluno = Aluno("Maria", 20, "Engenharia")
professor = Professor("Carlos", 45, 7000.00)

print(aluno.info())
print(professor.info())

# ========

print("### ---  Exercício 2 - Polimorfismo função genérica ---###")

aluno2_ex2 =  Aluno("João", 40, "TI")
professor2_ex2 = Professor("Marlon", 55, 14000.00)
pessoa2_ex2 = Pessoa("José", 30)

lista_obj_ex2 = [aluno, professor, aluno2_ex2, professor2_ex2, pessoa2_ex2]

def mostrar_info(pesso_obj):
    print(pesso_obj.info())

for obj in lista_obj_ex2:
    mostrar_info(obj)


# ✅ EXERCÍCIO 4 — Lista com filtro (extra)
# Objetivo: Criar uma lista com várias pessoas e imprimir apenas os professores com salário
# acima de R$ 5000.
# 💡 Dica:
# Use isinstance(obj, Professor) para verificar o tipo.

# professor1 = Professor("João", 50, 5500.00)
# professor2 = Professor("Marcos", 36, 4100.00)

# lista = [professor, professor1, professor2]

# for i in lista:
#     if i.salario > 5000.00:
#         print(i.nome)


#class Aluno(Pessoa):
    #def __init__(self, nome, idade, curso):
        #super().__init__(nome, idade)
        #self.curso = curso

    #def info(self):
        #return f"{self.nome}, {self.idade} anos, cursando {self.curso}"

#class Professor(Pessoa):
    #def __init__(self, nome, idade, salario):
        #super().__init__(nome, idade)
        #self.salario = salario

    #def info(self):
        #return f"{self.nome}, {self.idade} anos, salário R$ {self.salario}"
    
#aluno = Aluno("Maria", 20, "Engenharia")
#professor = Professor("Carlos", 45, 7000.00)