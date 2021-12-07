# -*- encoding: utf-8 -*-
"""
Sistema de Arquivos - Manipulação

import os

# Descobrindo se um arquivo ou diretório existe

print(os.path.exists('frutas.txt'))
print(os.path.exists('arquivo.txt'))

# Diretório

os.chdir('..')
print(os.path.exists('Geek University'))
print(os.path.exists('Geek University/university.txt'))
print(os.path.exists('outro'))

# Criando arquivos

# Forma 1
open('arquivo.teste.txt', 'w').close()

# Forma 2
open('arquivo.teste2.txt', 'a').close()

# Forma 3
with open('arquivo.teste3.txt', 'a') as arquivo:
    pass

# Forma mais adequada
os.mknod('arquivo.teste4.txt')

# Obs: se criando um arquivo via mknod() se o arquivo já existir teremos o erro FileExistsError.

# Criando diretórios

os.mkdir('templates')

# OBS: A função mkdir() cria um diretório se este não existir. Caso exista, FileExistsError.

# OBS: Se não tivermos permissão para criar o diretório, teremos o PermissionError

# Renomeando arquivos e diretórios

os.chdir('..')
os.rename('Geek University', 'geek_university')

OBS: Se o diretório que querem,os renomear não estiver vazio, teremos um OSError

# ATENÇÃO! Tome cuidado com os comandos de deleção. Ao deletarmos um arquivo ou diretório, eles
# não vão para a lixeira. Eles somem.

os.remove('nome do arquivo')

# OBS: Se você estiver no Windows e o arquivo que você for delear estriver em uso, você terá um erro.True

# OBS: Caso o arquivo não exista, teremos o FileNotFoundError

# Se você informar um diretório ao invés de um arquivo, teremos um IsADirectoryError

# Removendo diretórios vazios

os.rmdir('nome do diretório')

# OBS: Se o diretório tiver qualquer conteúdo teremos um OSError

# OBS: Se o diretório não existir teremos um FileNotFoundError

# Removendo uma árvore de diretórios
for arquivo in os.scandir('nome do arquivo'):
    if arquivo.is_file():
        os.remove(arquivo.path)

# Podemos remover uma árvore de diretórios vazios

os.removedirs('nome do diretório/nome do diretório')

# Se algum dos diretórios contiver arquivos ou outros diretórios, o processo para.

sudo apt-get install lsb-core

# Importando a biblioteca send2trash
from send2trash import send2trash (Envia arquivos e diretórios para a lixeira)

os.remove("nome do arquivo") # Não vai para a lixeira. É deletado imediatamente

os.send2trash('cesta2.txt') # Vai pra lixeira. Pode ser restaurado

# OBS: No caso do send2trash, se o arquivo não existir: OSError

import tempfile

with tempfile.TemporaryDirectory() as tmp:
    print(f'Criei um diretório temporário em {tmp}')
    with open(os.path.join(tmp, 'arquivo temporário.txt'), 'w') as arquivo:
        arquivo.write('Geek University\n')
    input()

# Estamos criando um diretório temporário, abrindo o mesmo e dentro dele criando um arquivo para
# escrevermos um texto. No final, usamos um input() só para mantermos os arquivos temporários 'vivos'
# dentro dos blocos with.

# OBS: possivelmente, o código acima não irá funcionar se você estiver utilizando o Windows. Por conta
# desse sistema trabalhar de forma diferente com arquivos temporários.

# Criando um arquivo temporário

with tempfile.TemporaryFile() as tmp:
    tmp.write(b'nome do arquivo\n')
    tmp.seek(0)
    print(tmp.read())

# OBS: Em arquivos temporários só conseguimos escrever bits. Por isso utilizamos o 'b'

# Sem o bloco with

arquivo = tempfile.TemporaryFile()
arquivo.write(b'nome do arquivo\n')
arquivo.seek(0)
print(arquivo.read())
arquivo.close()

# Trabalhando com arquivos e diretórios temporários

arquivo = tempfile.NamedTemporaryFile()
arquivo.write(b'nome do arquivo\n')
print(arquivo.name)
print(arquivo.read())
input()
arquivo.close()
"""

