"""
Trabalhando com módulos built-in

São módulos integrados que já vêm instalados no Python.

/Python|Módulos buiit-in

# Utilizando alias (apelidos) para módulos/funções

import random as rdm

print(rdm.random())

# Podemos importar todas as funções de um módulo utilizando o *

from random import *

print(random())

from random import randint as rdi, random as rdm

print(rdi(5, 89))

print(rdm())

# Costumamos utilizar tuple para colocarmos múltiplos imports de um mesmo módulo

from random import (
    random,
    randint,
    shuffle,
    choice
)

print(random())

print(randint(3, 7))

lista = [1, 2]
shuffle(lista)
print(lista)

print(choice('Univerisity'))
"""
