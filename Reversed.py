"""
Reversed

OBS: Não confunda com a função reverse() que estudamos nas listas.

A função reverse() só funciona com listas.

Já a função reversed() funciona com qualquer iterável.

Sua função é inverter o iterável

A função reversed() retorna um iterável chamado List Reverse Iterator (no caso de listas) ou um
Reverse Object (no caso de tuplas).

lista = [1, 2, 3, 4, 5]
tupla = (1, 2, 3, 4, 5)

res = reversed(lista)
restupla = reversed(tupla)

print(res)
print(type(res))    # List Reverse Iterator

print(restupla)
print(type(restupla))       # Reverse Object

# Podemos converter o elemento retornado para uma lista, tupla ou conjunto

# Lista
print(list(reversed(lista)))

# Lista
print(tuple(reversed(lista)))

# Conjunto
print(set(reversed(lista)))     # Em conjuntos não definimos a ordem dos elementos

# Podemos iterar sobre o reversed

for letra in reversed('Geek University'):
    print(letra, end='')

# Podemos fazer o mesmo sem o uso do for

print(''.join(reversed('Geek University')))

# Já vimos como faer isso mais fácil com o slice de strings

print('Geek University'[::-1])

# Podemos também utilizar o reversed() para fazer um loop for reverso

for n in reversed(range(0, 10)):
    print(n)

# Apesar que também já vimos como fazer utilizando o próprio range()

for n in range(9, -1, -1):
    print(n)
"""
