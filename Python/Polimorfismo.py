class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    
    def info(self):
        return f"{self.nome}, {self.idade} anos"

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

class Aluno(Pessoa):
    def __init__(self, nome, idade, curso):
        super().__init__(nome,idade)
        self.curso = curso

    def info(self):
        return f"{super().info()}, cursando {self.curso}"

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

professor1 = Professor("João", 50, 5500.00)
professor2 = Professor("Marcos", 36, 4100.00)

lista = [professor, professor1, professor2]

for i in lista:
    if i.salario > 5000.00:
        print(i.nome)