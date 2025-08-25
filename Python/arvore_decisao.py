# Arvore de decisão atua como um fluxograma de perguntas sim ou não.
# É um modelo que aprende a tomar decisões fazendo uma serie de perguntas sequencias sobre os dados.

# Imagine que você está tentando adivinhar um animal, e só pode fazer perguntas de sim/não:

# Pergunta: "O animal tem penas?" -> Sim

# Pergunta: "Ele pode voar?" -> Não

# Pergunta: "Ele é preto e branco?" -> Sim

# Conclusão: "Então, é um pinguim!"

#  O "treinamento" é o processo onde o algoritmo aprende, a partir dos dados, quais são as melhores perguntas a se fazer e em qual ordem para chegar à resposta correta o mais rápido possível.

#  Vantagens:
# Você pode literalmente visualizar a árvore e entender exatamente por que o modelo tomou uma decisão
# A escala das variáveis não importa.

# Desvantagem:
# Se não for controlada, a árvore pode crescer demais e ficar superespecializada nos dados de treino.

# O objetivo é criar um fluxograma de decisões para identificar a espécie de um pinguim.

import pandas as pd
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier, plot_tree 
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt

df = sns.load_dataset('penguins')
df.dropna(inplace=True)

X = df[['bill_length_mm', 'bill_depth_mm', 'flipper_length_mm', 'body_mass_g']]
y = df['species']

# 2. Divisão em Treino e Teste
X_treino, X_teste, y_treino, y_teste = train_test_split(X, y, test_size=0.3, random_state=42)

# 3. Criação do Modelo de Árvore de Decisão
modelo_arvore = DecisionTreeClassifier(max_depth=3, random_state=42)

# 4. Treinamento
modelo_arvore.fit(X_treino, y_treino)

# 5. Avaliação
previsoes = modelo_arvore.predict(X_teste)
acuracia = accuracy_score(y_teste, previsoes)
print(f"\nAcurácia do modelo de Árvore de Decisão: {acuracia:.2%}")

plot_tree(modelo_arvore, feature_names=X.columns, class_names=y.unique)
plt.show()
