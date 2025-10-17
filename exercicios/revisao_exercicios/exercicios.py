# Exercício 1: Herança e Polimorfismo em um Sistema de Notificações

# Cenário: Você está a desenvolver o backend de uma aplicação que precisa de enviar diferentes tipos de notificações para os seus utilizadores: 
# Email, SMS e Push (notificações de telemóvel). Todas são "notificações", mas cada uma tem um comportamento e atributos únicos.

# Objetivo: Criar um sistema hierárquico de classes que garanta que qualquer tipo de notificação possa ser "enviada", mas que o processo de envio seja específico para cada uma.

# Tarefas:

# 1.  Crie uma classe-mãe abstrata `Notificacao` (usando o módulo `abc`).
#      Ela deve ter um construtor que recebe `destinatario` e `mensagem`.
#      Ela deve ter um método abstrato chamado `enviar()`. Um método abstrato força as classes filhas a implementarem a sua própria versão dele.

# 2.  Crie três classes filhas que herdam de `Notificacao`:
#      `NotificacaoEmail(Notificacao)`:
#          O seu construtor deve receber, além de `destinatario` e `mensagem`, um `assunto`.
#          Implemente o método `enviar()` para que ele imprima uma mensagem formatada como:
#             `Enviando E-MAIL para: [destinatario] | Assunto: [assunto] >> "[mensagem]"`
#      `NotificacaoSMS(Notificacao)`:
#          O seu construtor não precisa de atributos extras.
#          Implemente o método `enviar()` para que ele imprima:
#             `Enviando SMS para: [destinatario] >> "[mensagem]"`
#      `NotificacaoPush(Notificacao)`:
#          O seu construtor deve receber, além dos atributos-padrão, um `dispositivo_id`.
#          Implemente o método `enviar()` para que ele imprima:
#             `Enviando PUSH para o dispositivo [dispositivo_id] >> "[mensagem]"`

# 3.  Crie a Função Polimórfica:
#      Crie uma função `enviar_notificacao_em_lote(lista_de_notificacoes)` que recebe uma lista contendo diferentes tipos de objetos de notificação.
#      Esta função deve iterar pela lista e chamar o método `.enviar()` de cada objeto.

# 4.  Teste o Sistema:
#      Crie uma lista com pelo menos uma instância de cada tipo de notificação (`NotificacaoEmail`, `NotificacaoSMS`, `NotificacaoPush`).
#      Passe essa lista para a sua função `enviar_notificacao_em_lote` e observe como a mesma chamada (`.enviar()`) produz saídas completamente diferentes, dependendo do objeto.


# ---
#  Exercício 2: Polimorfismo com "Duck Typing" num Renderizador Gráfico

# Cenário: Imagine que está a construir um motor de renderização para um editor de imagens ou um jogo. O motor precisa de desenhar diferentes formas geométricas no ecrã (`Círculo`, `Quadrado`, `Triângulo`). A função de renderização não deve precisar de saber qual é a forma, apenas que a forma "sabe como se desenhar".

# Objetivo: Praticar o polimorfismo através do "Duck Typing", onde o tipo da classe não importa, contanto que ela tenha os métodos esperados.

# Tarefas:

# 1.  Crie três classes de formas geométricas independentes (elas não devem herdar de uma classe-mãe comum):
#      `Circulo`:
#          O construtor deve receber `x`, `y` (coordenadas do centro) e `raio`.
#          Deve ter um método `desenhar()` que imprime:
#             `Desenhando Círculo no ponto ([x], [y]) com raio [raio].`
#      `Quadrado`:
#          O construtor deve receber `x`, `y` (coordenadas do canto superior esquerdo) e `lado`.
#          Deve ter um método `desenhar()` que imprime:
#             `Desenhando Quadrado no ponto ([x], [y]) com lado de [lado]px.`
#      `Texto`: (Aqui está a inovação!)
#          O construtor deve receber `x`, `y` e o `conteudo` do texto.
#          Deve ter um método `desenhar()` que imprime:
#             `Escrevendo texto "[conteudo]" na posição ([x], [y]).`

# 2.  Crie a Função Polimórfica de Renderização:
#      Crie uma função `renderizar_cena(objetos_para_desenhar)` que recebe uma lista de objetos.
#      A função deve iterar por essa lista e, para cada objeto, chamar o seu método `.desenhar()`.

# 3.  Teste o Renderizador:
#      Crie uma lista contendo várias instâncias das suas classes: dois `Circulo`s, um `Quadrado` e um `Texto`.
#      Passe esta lista para a função `renderizar_cena` e observe a magia do Duck Typing: a função consegue "desenhar" todos os objetos, incluindo o `Texto`, sem nunca verificar o tipo de cada um. Ela apenas assume que, se está na lista, "sabe como se desenhar".
# Com certeza! Adorei o entusiasmo. Manter a prática é a chave para a maestria.

# Vamos continuar a inovar. Preparei mais dois cenários do mundo real que exploram a herança e o polimorfismo de maneiras diferentes e muito práticas.

# ---
# Exercício 3: Herança e Polimorfismo num Jogo de RPG

# Cenário: Você é um desenvolvedor de jogos e está a criar o sistema de combate para um novo RPG. Existem diferentes classes de personagens (Guerreiro, Mago, Arqueiro). Todos são "personagens" e todos podem "atacar", mas a forma como atacam é única para cada classe.

# Objetivo: Usar a herança para criar uma base comum para os personagens e o polimorfismo para definir os seus ataques únicos.

# Tarefas:

# 1.  Crie uma classe-mãe `Personagem`:
#      No construtor, deve receber `nome` e `pontos_de_vida`.
#      Deve ter um método `status()` que imprime as informações básicas: `"[Nome] | HP: [Pontos de Vida]"`.
#      Deve ter um método `atacar(alvo)` que, por defeito, imprime uma mensagem genérica como `"[Nome] ataca [Nome do Alvo], mas não causa dano."`. A variável `alvo` será outro objeto `Personagem`.

# 2.  Crie duas classes filhas que herdam de `Personagem`:
#      `Guerreiro(Personagem)`:
#          O construtor deve receber, além dos atributos-padrão, a `forca`.
#          Sobrescreva o método `atacar(alvo)` para que ele imprima:
#             `"[Nome] desfere um golpe poderoso em [Nome do Alvo] com força [Força]!"`
#      `Mago(Personagem)`:
#          O construtor deve receber, além dos atributos-padrão, a `magia`.
#          Sobrescreva o método `atacar(alvo)` para que ele imprima:
#             `"[Nome] lança a magia '[Magia]' contra [Nome do Alvo]!"`

# 3.  Crie a Função Polimórfica de Combate:
#      Crie uma função `simular_combate(personagem1, personagem2)` que recebe dois objetos do tipo `Personagem`.
#      Dentro da função, faça o `personagem1` atacar o `personagem2` e, em seguida, o `personagem2` atacar o `personagem1`.

# 4.  Teste a Simulação:
#      Crie uma instância de `Guerreiro` e uma de `Mago`.
#      Chame a função `simular_combate` com estes dois personagens.
#      Desafio extra: Crie uma lista com vários guerreiros e magos. Faça um "todos contra todos", onde cada personagem da lista ataca todos os outros.

# ---
# Exercício 4: Polimorfismo num Pipeline de Processamento de Dados

# Cenário: Você está a construir um pipeline de ETL (Extração, Transformação, Carga) para uma empresa de análise de dados. O sistema precisa de ser capaz de processar diferentes tipos de ficheiros de dados (CSV, JSON, XML). O processo de "ler" e "validar" cada tipo de ficheiro é diferente, mas todos devem passar por um fluxo de trabalho padronizado.

# Objetivo: Usar classes e polimorfismo para criar um sistema de processamento de dados flexível e extensível.

# Tarefas:

# 1.  Crie três classes de processadores de ficheiros (sem herança):
#      `ProcessadorCSV`:
#          O construtor recebe o `caminho_do_ficheiro`.
#          Deve ter um método `processar()` que imprime:
#             `"Lendo ficheiro CSV de [caminho]... Validando colunas... Processamento concluído."`
#      `ProcessadorJSON`:
#          O construtor recebe o `caminho_do_ficheiro`.
#          Deve ter um método `processar()` que imprime:
#             `"Lendo ficheiro JSON de [caminho]... Validando estrutura chave-valor... Processamento concluído."`
#      `ProcessadorXML`:
#          O construtor recebe o `caminho_do_ficheiro`.
#          Deve ter um método `processar()` que imprime:
#             `"Lendo ficheiro XML de [caminho]... Validando tags... Processamento concluído."`

# 2.  Crie a Função Polimórfica do Pipeline:
#      Crie uma função `executar_pipeline(processadores)` que recebe uma lista de objetos processadores.
#      A função deve iterar pela lista e, para cada `processador` na lista, chamar o seu método `.processar()`.

# 3.  Teste o Pipeline:
#      Imagine que uma pasta contém vários ficheiros para serem processados: `dados.csv`, `relatorio.json`, `config.xml` e `backup.json`.
#      Crie uma lista de "trabalhos", onde cada trabalho é uma instância de um dos processadores (`ProcessadorCSV('dados.csv')`, `ProcessadorJSON('relatorio.json')`, etc.).
#      Passe esta lista para a sua função `executar_pipeline` e observe como o sistema processa cada ficheiro de forma diferente, usando a mesma chamada de função.
