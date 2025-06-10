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