"""
Leitura de Arquivos

Para ler o conteúdo de um arquivo em Python utilizamos a função integrada open().
Que literalmente significa 'abrir'.

open() -> A forma mais simples de utilização, nós passamos apenas um parâmetro de entrada, que neste caso é o
caminho do arquivo a ser lido. Essa função retorna um _io.TextIOWrapper e é com ele que trabalhamos então.

https://docs.python.org/3/library/functions.html#open

# OBS: Por padrão, a função open() abre o arquivo para leitura. Esse arquivo deve existir, ou então teremos
 o erro FileNotFoundError

arquivo = open('texto.txt', encoding='utf-8)

print(arquivo)      # <_io.TextIOWrapper name='texto.txt' mode='r' encoding='utf-8'>

print(type(arquivo))        # <class '_io.TextIOWrapper'>

mode r -> Modo de leitura. r -> read() -> Ler       # Por padrão, o modo de abertura do open() é Leitura

# Para ler o conteúdo de um arquivo, após sua abertura, devemos utilizar a função read()

ret = arquivo.read()

print(type(ret))    # String

print(ret)

print(arquivo.read())   # Não será executado pois o arquivo já foi lido em ret.

# OBS: O Python utiliza um recurso para trabalhar ncom arquivos chamado cursor. Esse cursor funciona
# como o cursor quando estamos escrevendo.

# OBS: A função read() lê todo o conteúdo do arquivo.
"""
with open('texto.txt', encoding='utf=8') as arquivo:
    arquivo.seek(3)
    print(arquivo.read(23))
    print(arquivo.closed)
print(arquivo.closed)