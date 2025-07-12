# ✅ EXERCÍCIO 7 — Polimorfismo com Operadores
# Objetivo: Observar como operadores comuns em Python (como + ou *) exibem comportamento polimórfico dependendo dos tipos dos operandos.

# 📋 Enunciado:

# Crie duas classes: Caixa e Produto.

# A classe Caixa deve ter um atributo itens (uma lista, inicializada vazia) e um atributo volume_maximo.
# Implemente o método __str__(self) na classe Caixa para retornar uma string descrevendo a caixa e seus itens (ex: "Caixa com X itens / Volume Máximo: Y").
# Implemente um método adicionar_item(self, item) na classe Caixa que adiciona um item à lista itens.
# Polimorfismo com +: Sobrescreva o operador de adição (__add__) na classe Caixa. Quando duas caixas são somadas (caixa1 + caixa2), o resultado deve ser uma nova Caixa contendo todos os itens de ambas as caixas originais, e o volume_maximo da nova caixa pode ser a soma dos volumes das caixas originais.
# A classe Produto deve ter atributos nome e volume.

# Implemente o método __str__(self) para retornar o nome do produto.
# Crie algumas instâncias de Produto.

# Crie duas instâncias de Caixa. Adicione diferentes produtos a elas.

# Demonstre o polimorfismo:

# Imprima as caixas individualmente (usando o __str__ que você definiu).
# Crie uma terceira caixa somando as duas primeiras (caixa3 = caixa1 + caixa2).
# Imprima a terceira caixa e verifique se ela contém os itens de ambas e o volume combinado.
# 💡 Dica:
# Para sobrescrever operadores, você implementa "métodos mágicos" (aqueles com duplo sublinhado, como __add__, __str__, __len__, etc.).

class Caixa:
    def __init__(self, volume_maximo):
        self.itens = []
        self.volume_maximo = volume_maximo
    
    def __str__(self)->str:
        return f"Caixa com {len(self.itens)} itens / Volume Máximo: {self.volume_maximo}"
    
    def adicionar_item(self, item):
        self.itens.append(item)

    def __add__(self, outra_caixa):
        novo_volume_maximo = self.volume_maximo + outra_caixa.volume_maximo
        nova_caixa = Caixa(novo_volume_maximo)
        nova_caixa.itens = self.itens + outra_caixa.itens
        return nova_caixa

class Produto():
    def __init__(self, nome, volume):
        self.nome = nome
        self.volume = volume

    def __str__(self)->str:
        return f"Nome do produto {self.nome} / Volume:{self.volume}"
        
produto1 = Produto("cobertor", 4)
produto2 = Produto("mochila", 2)

caixa1 = Caixa(5)
caixa2 = Caixa(3)

caixa1.adicionar_item(produto1)
print(caixa1)

caixa2.adicionar_item(produto2)
print(caixa2)

nova_caixa = caixa1 + caixa2
print(nova_caixa)

