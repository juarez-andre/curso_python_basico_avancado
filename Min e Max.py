"""
Min e Max

max() -> Retorna o maior valor em um iterável ou o maior de dois ou mais elementos.

# Exemplos

tupla = (1, 8, 4, 89, 129)
print(max(tupla))

lista = [1, 8, 4, 89, 129]
print(max(lista))

conjunto = {1, 8, 4, 89, 129}
print(max(conjunto))

dicionario = {'a': 1, 'b': 8, 'c': 4, 'd': 89, 'e': 129}
print(max(dicionario.values()))

# Faça um programa que receba dois valores do usuário e mostre o maior

val1 = int(input('Informe o primeiro valor: '))
val2 = int(input('Informe o segundo valor: '))

print(max(val1, val2))

print(max('a', 'ab', 'abc'))    # abc
print(max('a', 'b', 'g'))       # g
print(max('Geek University'))       # y

min() -> Retorna o menor valor em um iterável ou o menor de dois ou mais elementos.

# Exemplos

tupla = (1, 8, 4, 89, 129)
print(min(tupla))

lista = [1, 8, 4, 89, 129]
print(min(lista))

conjunto = {1, 8, 4, 89, 129}
print(min(conjunto))

dicionario = {'a': 1, 'b': 8, 'c': 4, 'd': 89, 'e': 129}
print(min(dicionario.values()))

# Faça um programa que receba dois valores do usuário e mostre o maior

val1 = int(input('Informe o primeiro valor: '))
val2 = int(input('Informe o segundo valor: '))

print(min(val1, val2))

print(min('a', 'ab', 'abc'))    # a
print(min('a', 'b', 'g'))       # a
print(min('Geek University'))       # O menor aqui é o ' '

# Outros exemplos

nomes = ['Arya', 'Samson', 'Dora', 'Tim', 'Olivander']

print(max(nomes))       # Tim

print(min(nomes))       # Arya

print(max(nomes, key=lambda nome: len(nome)))

print(min(nomes, key=lambda nome: len(nome)))

musicas = [{"título": "Thunderstruck", "tocou": 3},
           {"título": "Dead Skin Mask", "tocou": 2},
           {"título": "Back in Black", "tocou": 4},
           {"título": "Too old to Rock 'n Roll, Too Young To Die", "tocou": 32}]

print(max(musicas, key=lambda x: x['tocou']))
print(min(musicas, key=lambda x: x['tocou']))

# DESAFI0! Imprima somente o título da música mais e menos tocada

print(max(musicas, key=lambda x: x['tocou'])['título'])
print(min(musicas, key=lambda x: x['tocou'])['título'])

# DESAFIO! Como encontrar a música mais tocada e a menos tocada sem usar max, min e lambda.

max = 0
mt = ''
for x in musicas:
    if x['tocou'] > max:
        mt = x['título']
print(mt)

contador = 1
for x in musicas:
    if contador == 1:
        menost = x['título']
        min = x['tocou']
    else:
        if x['tocou'] < min:
            menost = x['título']
    contador += 1

print(menost)
"""
