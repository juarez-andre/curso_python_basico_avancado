"""
O bloco with

# 1 -  Abrimos o arquivo
# 2 - Manipulamos o arquivo
# 3 - Fechamos o arquivo

O bloco with é utilizado para criar um contexto de trabalho onde os recursos utilizados são fechados
após o bloco with.

# O bloco with - Forma Pythônica de manipular arquivos

with open('texto.txt') as arquivo:
    print(arquivo.readlines())
    print(arquivo.closed)       # False - pois ele só fecha quando sai do bloco with

print(arquivo.closed)   # True

print(arquivo.read())   # ValueError - Pois o arquivo está fechado
"""
