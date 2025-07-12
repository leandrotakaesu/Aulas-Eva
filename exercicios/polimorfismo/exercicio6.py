# ✅ EXERCÍCIO 6 — Polimorfismo com Herança e Métodos Abstratos (simulado)
# Objetivo: Praticar polimorfismo em uma hierarquia de classes onde as subclasses fornecem implementações específicas de um método definido (ou esperado) na superclasse.

# 📋 Enunciado:

# Crie uma classe base InstrumentoMusical.

# Ela deve ter um construtor que aceita um nome para o instrumento.
# Ela deve ter um método tocar() que, por padrão, imprime uma mensagem como "Nome do instrumento está produzindo um som indefinido." 
# ou levanta um NotImplementedError para indicar que subclasses devem implementá-lo.
# Crie duas classes filhas que herdam de InstrumentoMusical:

# Violao: O método tocar() deve imprimir "As cordas do Violão estão vibrando: Dó, Ré, Mi..."
# Bateria: O método tocar() deve imprimir "A Bateria está marcando o ritmo: TUM, TA, TUM TUM TA!"
# Crie uma função apresentar_instrumento(instrumento) que recebe um objeto do tipo InstrumentoMusical (ou suas subclasses) e chama seu método tocar().

# Crie uma lista com instâncias de Violao e Bateria. Itere sobre a lista e chame apresentar_instrumento() para cada um.

# 💡 Exemplo de Saída Esperada (para a iteração):

# As cordas do Violão estão vibrando: Dó, Ré, Mi...
# A Bateria está marcando o ritmo: TUM, TA, TUM TUM TA!
# (Opcional avançado: Pesquise sobre o módulo abc em Python para criar classes abstratas de verdade e marcar tocar() como um @abstractmethod.)


class InstrumentoMusical:
    def __init__(self, nome):
        self.nome = nome

    def tocar(self):
        print(f"{self.nome} está produzindo um som indefinido")
    
class Violao(InstrumentoMusical):
    def __init__(self, nome):
        super().__init__(nome)

    def tocar(self):
        print(f"{self.nome}: As cordas do Violão estão vibrando: Dó, Ré, Mi...")
    
class Bateria(InstrumentoMusical):
    def __init__(self, nome):
        super().__init__(nome)

    #def tocar(self):
        #print(f"{self.nome}: A Bateria está marcando o ritmo: TUM, TA, TUM TUM TA!")

#Função genérica que pode "apresentar" qualquer instrumento que saiba "tocar".
    
def apresentar_instrumento(instrumento):
    instrumento.tocar()

instrumento1 = Violao("violao")
instrumento2 = Bateria("bateria")

lista = [instrumento1, instrumento2]

for objeto in lista:
    apresentar_instrumento(objeto)
