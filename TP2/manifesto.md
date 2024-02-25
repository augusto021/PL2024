# TPC2: Conversor de MD para HTML

## Autor:
* João Augusto Macedo Moreira
* a93326

### Resumo:

Inicialmente, define-se o caminho do arquivo Markdown a ser processado e posteriormente, aberto e lido. De seguida, define-se padrões de expressões regulares para transformar o Markdown em HTML, como cabeçalhos, negrito, itálico, listas ordenadas, links e imagens.
    
É criado uma função, new_pattern, que aplica as substituições definidas pelos padrões nas linhas do texto. Aplica as substituições ao texto do arquivo Markdown. Divide o texto em linhas e processa para adicionar tags \<ol> e \</ol> para listas ordenadas. E por fim, escreve o conteúdo HTML processado em um novo arquivo HTML.

Em suma, o código lê um arquivo Markdown, aplica uma série de substituições de padrões para transformá-lo em HTML e, em seguida, escreve o HTML resultante num novo arquivo.
