print("Hello World")

def maior_valor(lista):
    maior = lista[0]
    i = 1
    tamanho = len(lista)

    while i < tamanho:
        if lista[i] > maior:
            maior = lista[i]
        i = i + 1
    return maior

lista = [10, 20, 30, 15]
maior = maior_valor(lista)
print(maior)

class Veiculo():

    def __init__(self, nome, marca, km):
        self.nome = nome
        self.marca = marca
        self.km = km
    
    def __str__(self):
        return f"O nome do veículo é {self.nome} da marca {self.marca} e tem quilometragem de {self.km}"

carro = Veiculo("Gol", "VW", 25000)
print(carro.__str__())