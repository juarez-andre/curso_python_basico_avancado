"""
Map

Com map, fazemos mapeamento de valores para função.

import math

def area(r):
    """"Calcula a área de um círculo com área r""""
    return math.pi * (r ** 2)

print(area(2))
print(area(5.3))

raios = [2, 5, 7.1, 0.3, 10, 44]

# Forma comum

areas = []
for r in raios:
    areas.append(area(r))
print(areas)

# Forma 2 - Map

# Map é uma função que recebe dois parâmetros: O primeiro a função, o segundo um iterável. Retorna um Map Object

raios = [2, 5, 7.1, 0.3, 10, 44]

areas = map(area, raios)

print(areas)
print(type(areas))
print(list(areas))

# Forma 3 - Map com Lambda

print(list(map(lambda r: math.pi * (r ** 2), raios)))

# OBS: Após utilizar a função map(), depois da primeira utilização dp resultado, ele zera.

# Para fixar - Map

# Temos dados iteráveis:

# dados: a1, a2, ..., an

# Temos uma função:

# Função: f(x)

# Utilizamos a função map(f, dados) onde map irá 'mapear' cada elemento dos dados e aplicar a função.

# O map object: f(a1), f(a2), f(...), f(n)

# Mais um exemplo

cidades = [('Berlim', 29), ('Cairo', 36), ('Buenos Aires', 19), ('Los Angeles', 26), ('Tokyo', 27),
           ('Nova York', 28), ('Londres', 22)]
print(list(map(lambda y: (y[0], y[1] * 1.8 + 32), cidades)))

# Comprehensions x Lambdas x Maps

Para submeter dados de uma lista a um processamento simples, de fácil elaboração, basta se fazer um list comprehension,
já para que possamos ordenar os valores de uma lista baseada determinado elemento, a lambda é perfeita para destacar a key.
Fora que também é um ótimo tipo de função.

Comprehensions =  processar dados de uma lista e colocá-los em uma nova lista
lambda = função anônima que serve para estabeler metodologias de tratamento de dados de uma lista (que por sua vez poderão
 ser utilizadas em maps), e também selecionar a key desejada para ordenar uma lista.

 map = possue basicamente a  mesma função que as comprehension, porém é estruturada de uma forma diferente e retorna um
 map object, que por sua vez deverá ser convertido no tipo de dados desejado (ISSO É BEM ÚTIL).

"""
