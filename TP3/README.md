# TPC3: Somador on/off


## Autor:
* João Augusto Macedo Moreira
* a93326

### Resumo:

O código começa com a especificação do caminho do arquivo que contém o texto a ser analisado (somador.txt), e o conteúdo deste arquivo é lido e armazenado na variável text.

É definido um padrão de expressão regular (pattern) que corresponde a três tipos de padrões:
* A palavra "on" ou "off" em qualquer combinação de maiúsculas e minúsculas.
* Sequências de um ou mais dígitos.
* O carácter "=".

Em seguida, são inicializadas duas variáveis: state_sum, que controla se a soma está ligada ou desligada, e sum, que armazena o valor da soma atual.

O loop for percorre todas as correspondências encontradas pelo padrão na variável text.
Dentro do loop, verifica se a correspondência atual é a palavra "off". Se for, state_sum é definido como False e a soma é inicializada para zero.
Se a correspondência atual for a palavra "on", state_sum é definido como True.
Se a correspondência atual for o carácter "=", e a soma estiver ligada (state_sum é True), o resultado da soma até o momento é imprimido.
Se a soma estiver ligada (state_sum é True) e a correspondência atual não for "=", então a correspondência (que deve ser uma sequência de dígitos) é convertida para um número inteiro e adicionada à soma atual (sum). E posteriormente, imprimida.

Em suma, este código processa o texto, soma sequências de dígitos, e imprime o resultado sempre que encontra "=", respeitando os comandos "On" e "Off" para ligar e desligar a soma.
