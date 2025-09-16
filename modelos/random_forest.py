# Conceito Central: Combinar as previsões de muitas Árvores de Decisão para obter uma previsão mais robusta e precisa.

# O que ela faz? Explicar o conceito de "ensemble" (conjunto). Vamos mostrar que a Random 
# Forest treina centenas de árvores, cada uma com uma visão ligeiramente diferente dos dados.
#  A previsão final é uma "votação" (para classificação) ou uma "média" (para regressão) das
# árvores individuais.

# Analogia: O "Comitê de Especialistas". A decisão do comitê é quase sempre melhor que a de 
# um único especialista.

# Quando escolher?

# Quando seu principal objetivo é a máxima precisão preditiva. É o "canivete suíço" que funciona bem na maioria dos problemas.

# Quando você não está tão preocupado em explicar o "porquê" de cada previsão individual (é uma "caixa-preta").

# Quando você quer um modelo que seja muito resistente a "overfitting" (decorar os dados de treino).