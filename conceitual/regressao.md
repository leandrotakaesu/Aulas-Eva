Categoria 1:
Quero prever um numero (Problema de Regressão)

Qual o preço de um imóvel?
Quantas vendas vou ter no próximo mês?
Qual a temperatura amanhã?


O Problema: Prever o Preço de uma Pizza
Imagine que temos dados de várias pizzas e queremos criar um modelo que preveja o preço com base no seu diâmetro em centímetros.

Diâmetro (cm)	Preço (R$)
    15	        22.00
    20	        28.50
    25	        40.00
    30	        45.00
    35	        58.00

Modelo para tentar:

1. Regressão linear (LineaRegression) -> "O Economista Racional"
Explicação a partir de uma fórmula simples e direta.

Como "Pensa":

Ela olha para todos os pontos no gráfico (diâmetro vs. preço).

Tenta encontrar a melhor linha reta possível que passe o mais perto de todos os pontos.

A "inteligência" do modelo se resume a uma única fórmula matemática que ele aprendeu, como:
Preço = (Diâmetro * 1.5) + 5


2. Árvore de Decisão (DecisionTreeRegressor) -  "O Gerente Detalhista"
Não acredita em uma fórmula única, mas cria regras específicas para diferentes situações.
    Quando escolher
    Prós
    Contras


3. Random Forest (RandomForestRegressor)
    Quando escolher
    Prós
    Contras
