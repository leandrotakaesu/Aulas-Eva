#  Modelos de Classificação
# O que é Classificação?
# É a tarefa de ensinar um computador a prever uma categoria ou rótulo.

# Regressão - Prever um valor numérico contínuo

# Pergunta: "Qual o preço deste imóvel?"

# Pergunta: "Quantas vendas teremos?"

# Modelo: Regressão Linear

# Classificação

# Prever uma categoria discreta

# Pergunta: "Este e-mail é spam ou não spam?"

# Pergunta: "Este cliente vai cancelar ou não cancelar o serviço?"

# Modelo: Classificador K-NN, Árvore de Decisão, etc.

# K-Nearest Neighbors (K-NN) "K Vizinhos Mais Próximos".

# Como o K-NN funciona (Analogia):

# Imagine que você tem um novo aluno na escola e não sabe de qual turma ele é. O K-NN simplesmente olha para os 5 alunos mais próximos dele no pátio. Se 3 desses 5 alunos são da turma 'A' e 2 são da turma 'B', o K-NN decide que o novo aluno provavelmente é da turma 'A' (voto da maioria).

import pandas as pd
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, confusion_matrix
import matplotlib.pyplot as plt

df = sns.load_dataset('penguins')
df.dropna(inplace=True)

# --- Passo 1: Preparação dos Dados (X e y) ---
# Features (causas): as medidas do pinguim
X = df[['bill_length_mm', 'bill_depth_mm', 'flipper_length_mm', 'body_mass_g']]
# Target (efeito): a espécie que queremos prever
y = df['species']

# --- Passo 2: Divisão em Treino e Teste ---
X_treino, X_teste, y_treino, y_teste = train_test_split(X, y, test_size=0.3, random_state=42)

# --- Passo 3: Escolha e Criação do Modelo ---
# Escolhemos o classificador K-NN com k=5 (olhará para os 5 vizinhos mais próximos)
modelo_knn = KNeighborsClassifier(n_neighbors=5)

# --- Passo 4: Treinamento do Modelo ---
# A mesma função .fit()! O modelo "memoriza" as posições de todos os pinguins de treino.
modelo_knn.fit(X_treino, y_treino)
print("✅ Modelo K-NN treinado!")

# --- Passo 5: Avaliação do Modelo ---
# Fazendo as previsões no conjunto de teste
previsoes = modelo_knn.predict(X_teste)


# Enquanto a acurácia te dá a nota final (ex: "O modelo acertou 98% das vezes"), a matriz de confusão te mostra onde ele acertou e, mais importante, onde e como ele errou.
# Métrica 1: Acurácia (Accuracy)
# Qual a porcentagem de acertos do modelo?
acuracia = accuracy_score(y_teste, previsoes)
print(f"\nAcurácia do modelo: {acuracia:.2%}")

# Métrica 2: Matriz de Confusão
# Um relatório detalhado de acertos e erros.
matriz = confusion_matrix(y_teste, previsoes)
print("\nMatriz de Confusão:")
# Vamos visualizar a matriz com um heatmap para ficar mais claro
sns.heatmap(matriz, annot=True, fmt='d', xticklabels=modelo_knn.classes_, yticklabels=modelo_knn.classes_, cmap='Blues')
# matriz: O primeiro argumento são os dado
# annot=True: annot é abreviação de "annotate" (anotar). 
# fmt='d': fmt é abreviação de "format" (formato). 
# xticklabels=modelo_knn.classes_ e yticklabels=modelo_knn.classes_: Estes parâmetros definem os rótulos para os eixos X e Y.
# cmap='Blues': cmap significa "colormap" (mapa de cores).
plt.xlabel('Rótulo Previsto')
plt.ylabel('Rótulo Real')
plt.title('Matriz de Confusão')
plt.show()