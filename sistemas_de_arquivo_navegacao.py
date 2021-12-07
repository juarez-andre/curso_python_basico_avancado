# -*- encoding: utf-8 -*-
"""
Sistema de Arquivos e Navegação

Para fazer uso de manipulação de arquivos do sistema operacinal, precisamos importar e fazer uso do
módulo os.

os -> Operating System - Sistema Operacional

# Fazer o import
import os

# getcwd() -> Pega o current work directory - diretório de trabalho corrente
# Retorna o path (caminho) absoluto

print(os.getcwd())  # C:\Users\Juarez\PycharmProjects\pythonProject\geek_university

# Para mudar o diretório podemos utilizar o chdir()

os.chdir('..')

print(os.getcwd())  # C:\Users\Juarez\PycharmProjects\pythonProject

os.chdir('..')

print(os.getcwd())  # C:\Users\Juarez\PycharmProjects

# Podemos fazer isso até chegar no diretório raiz

# Podemos checar se um diretório é absoluto ou relativo

print(os.path.isabs("coloca o caminho aqui"))     # True (essa forma não funciona em Windows)

# OBS para usuários Windows: No caso de computador Windows, deve-se que ter cuidado ao verificar diretórios.

# Fazer com Windows:

print(os.path.isabs("C:\\Users\\PythonProjects"))

# Podemos identificar o sistema operacional com o módulo os

print(os.name)  # posix (Linux e Mac), nt (Windows)

# Podemos usar o os.uname() para ter mais detalhes do sistema operacional utilizado (aparentemente não funciona em Windows)

print(os.uname())

# No caso de Windows:
import sys

print(sys.platform)

# Podemos listar os arquivos e diretórios com listdir()

print(os.listdir()))

# Podemos listar os arquivos e diretórios com mais detalhes com scandir()

arquivos = list(os.scandir())

print(arquivos)
print(dir(arquivos[0]))

print(arquivos[0].inode)    # ??
print(arquivos[0].is_dir)   # É um diretório?
print(arquivos[0].is_file)  # É um arquivo?
print(arquivos[0].is.symlink)   # É um link simbólico?
print(arquivos[0].name) # Nome do arquivo
print(arquivos[0].path) # Caminho até o arquivo
print(arquivos[0].stat) # ??
"""

