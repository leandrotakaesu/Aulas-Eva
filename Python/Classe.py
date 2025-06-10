#class Pessoa:
    #def __init__(self, nome, idade):
        #self.nome = nome
        #self.idade = idade
    
    #def saudacao(self):
        #print(f"Olá, {self.nome}! Você tem {self.idade} anos!")

#pessoa1 = Pessoa("Leandro", 40)
#pessoa1.idade = 50

#pessoa1.saudacao()

class Funcionario:
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario

    def info(self):
         return f"{self.nome} ganha R$ {self.salario: 2f}"
    
class Gerente(Funcionario):
    def __init__(self, nome, salario, setor):
        super().__init__(nome,salario)
        self.setor = setor

    def info(self):
        return f"{super().info()} e é o Gerente do setor {self.setor}."
    
funcionario = Funcionario("João", 3000)
gerente = Gerente("Ana", 5000, "TI")

lista = [funcionario, gerente]

def mostrar_info(pessoa_objeto):
    print(pessoa_objeto.info())

for objeto in lista:
    mostrar_info(objeto)

# print(funcionario.info())
# print(gerente.info())