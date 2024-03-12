# TPC4: Analisador Léxico

## Autor:
* João Augusto Macedo Moreira
* a93326

### Resumo:

Inicialmente, são definidos tokens que posteriormente vão ser reconhecidos pelo analisador léxico, e para cada token, são definidas as expressões regulares que o descrevem. 

De seguida, são definidas as funções que serão usadas pelo analisador léxico para reconhecer os tokens na entrada. Essas recebem a entrada e tentam fazer uma correspondência com a expressão regular associada ao token. Se houver uma correspondência, é criado um token e retornado. Caso contrário, é gerado um erro devido ao caractér não ser reconhecido.
