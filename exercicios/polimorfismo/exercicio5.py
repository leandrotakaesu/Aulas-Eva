# ✅ EXERCÍCIO 5 — Polimorfismo com "Duck Typing"
# Objetivo: Entender como o Python lida com polimorfismo através do "Duck Typing" (se anda como um pato e grasna como um pato, então é um pato).

# 📋 Enunciado:
# Crie três classes diferentes: Pato, Cachorro e Aviao.

# A classe Pato deve ter um método fazer_som() que imprime "Quack!" e um método mover() que imprime "Pato nadando."
# A classe Cachorro deve ter um método fazer_som() que imprime "Au au!" e um método mover() que imprime "Cachorro correndo."
# A classe Aviao deve ter um método fazer_som() que imprime "VUUUUSH!" (som da turbina) e um método mover() que imprime "Avião decolando."
# Crie uma função chamada interagir_com_objeto(obj) que chama os métodos obj.fazer_som() e obj.mover().

# Crie uma lista com instâncias de Pato, Cachorro e Aviao. Itere sobre a lista e chame a função interagir_com_objeto() para cada objeto. 
# Observe que a função funciona para todos os objetos, mesmo que eles não herdem de uma classe comum (além de object).

# 💡 Dica:
# O Python não se importa com o tipo do objeto, contanto que ele tenha os métodos que estão sendo chamados.

