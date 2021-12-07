# -*- encoding: utf-8 -*-
"""
Modos de abertura de arquivos

r -> Abre para leitura - padrão
w -> Abre para escrita - sobrescreve caso o arquivo já exista
x -> Abre para escrita somente se o arquivo NÃO EXISTIR.
a -> Abre para escrita adicionando o conteúdo para o FINAL do arquivo.
+ -> Abre para o modo de atualização: Leitura e Escrita -   prof não explicou direito

OBS: Abrindo no modo 'a' -> append, se o arquivo não existir será criado. Caso exista, o novo conteúdo
será adicionado ao final do arquivo SEMPRE (não adianta nem usar o seek(), ou seja, com o modo 'a' não
controlamos o cursor).

http://docs.python.org/3/library/functions.html#open

# Exemplo x
with open('university.txt', 'w', encoding='utf-8') as arquivo:
    arquivo.write('Teste de conteúdo 2.\n')

Forma interessante usando o Try/Except:

try:
    with open('university.txt', 'x') as arquivo:
        arquivo.write('Escrevendo no arquivo')
except FileExistsError:
    print('O arquivo já existe')

# Exemplo a

with open('frutas.txt', 'a') as arquivo:
    while True:
        fruta = input('Informe uma fruta ou sair: ')
        if fruta != 'sair':
            arquivo.write(fruta)
            arquivo.write('\n')
        else:
            break
"""
