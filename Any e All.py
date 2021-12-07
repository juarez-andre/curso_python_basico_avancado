"""
Any e All

all() -> Retorna True se todos os elementos do iterável são verdadeiros ou ainda se o iterável está vazio

# Exemplos all()

print(all([0, 1, 2, 3, 4]))     # Todos os números são verdadeiros? False por causa do 0.

print(all([1, 2, 3, 4]))     # Todos os números são verdadeiros? True

#OBS: Um iterável vazio (seja string, lista, tupla etc) convertido em bool é falso, mas o all() entende como True

print(all([]))     # Todos os números são verdadeiros? True

nomes = ['Carlos', 'Camila', 'Cassiano', 'Cristina']

print(all([nome[0] == 'C' for nome in nomes]))

# Outro exemplo

print(all([letra for letra in '' if letra in 'aeiou']))     # String vazia =  True

print(all([num for num in [2, 4, 6, 8] if num % 2 == 0]))       # lista vazia = True

any() -> Retorna True se qualquer elemento do iterável for verdadeiro. Se o iterável estiver vazio, retorna False
"""

# Exemplos

print(any([0, 1, 2, 3]))    # True

print(any([0, False, {}, (), []]))      # False

nomes = ['Carlos, Camila', 'Carla', 'Vanessa']

print(any([nome[0] == 'C' for nome in nomes]))

print(any([num for num in [4, 2, 10, 6] if num % 2 == 0]))