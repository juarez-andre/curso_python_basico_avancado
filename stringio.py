# -*- encoding: utf-8 -*-
"""
StringIO

ATENÇÃO: Para ler ou escrever dados em arquivos do sistema operacional o software precisa ter permissão:
    - Permissão de leitura para ler o arquivo.
    - Permissão de escrita para ler o arquivo.

StringIO -> Utilizado para ler e criar arquivos em memória. Ou seja, não vai gravar no disco, e sim ficará na memória (?).

# Primeiro fazemos o import
from io import StringIO

mensagem = 'Esta é apenas uma string normal.'

# Podemos criar um arquivo em memória já com uma string inserida ou mesmo vazio para inserirmos texto depois

arquivo = StringIO(mensagem)    # Isso equivale a escrever: arquivo = open('arquivo.txt', 'w')

# Agora tendo o arquivo, podemos utilizar tudo que já sabemos
print(arquivo.read())

# Escrevendo outros textos
arquivo.write(' Outro texto')

# Podemos inclusive movimentar o cursor
arquivo.seek(0)

print(arquivo.read())

Repare como a StringIO nos permite ler e escrever no arquivo quantas vezes quisermos sem que ele
desapareça após o primeiro uso.
"""
