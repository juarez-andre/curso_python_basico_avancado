"""
Dictionary Comprehension

Pense no seguinte:

Se quisermos criar uma lista fazemos:

lista = [1, 2, 3, 4]

Se quisermos criar uma tupla:

tupla = (1, 2, 3, 4)

Se quisermos criar um set:

conjunto = {1. 2, 3, 4}

Se quisermos criar um dicionário:

dicionario = {'a': 1, 'b': 2}

# Sintaxe

{chave: valor for valor in iterável}

# Exemplos

dicionario = {'a': 1, 'b': 2, 'c': 3, 'd': 4}

quadrado = {chave: valor ** 2 for chave, valor in dicionario.items()}

print(quadrado)

numero = [1, 2, 3, 4, 5] # Lembrando que se houver valores repetidos na lista, o dict comprehension
desconsiderará os valores repetidos.

print({valor: valor ** 2 for valor in numero})

chaves = 'abcde'
valores = [1, 2, 3, 4, 5]

mistura = {chaves[i]: valores[i] for i in range(0, len(chaves))}
print(mistura)

# Exemplo com lógica condicional

numeros = [1, 2, 3, 4, 5]
res = {num: ('par' if num % 2 == 0 else 'ímpar') for num in numeros}
print(res)
"""
