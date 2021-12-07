"""
Utilizando Lambdas

Conhecidas por expressões lambdas, ou simplesmente lambdas, são funções sem nome, ou seja,
funções anônimas;

# Funções em Python

def funcao(x):
    return 3 * x + 1

print(funcao(4))

# Expressão Lambda

lambda x: 3 * x + 1

# Como utilizar a expressão lambda

calc = lambda x: 3 * x + 1

print(calc(4))

# Podemos ter expressões lambdas com múltiplas entradas

nome_completo = lambda nome, sobrenome: nome.strip().title() + ' ' + sobrenome.strip().title()

print(nome_completo('angelina', '    JOLIE'))

# Em funções python podemos ter nenhuma ou várias entradas, em lambdas também.

amar = lambda: 'Como não amar python?'

uma = lambda x:  3 * x + 1

duas = lambda x, y: (x * y) ** 0.5

tres = lambda x, y, z: 3 / (1 / x + 1 / y + 1 / z)

# n = lambda x1, x2, ..., xn <expressão>

print(amar())
print(uma(0))
print(duas(5, 7))
print(tres(3, 6, 9))

# OBS: Se passarmos mais ou menos argumentos do que parâmetros esperados, teremos TypeError

# Outro exemplo

autores = ['JK Rolling', 'Ray Bradbury', 'Arthur C. Clarke', 'Frank Herbert', 'Douglas Adams',
           'Orson Scott Card', 'H G Wells', 'Leigh Brackett']

autores.sort(key=lambda sobrenome: sobrenome.split(' ')[-1].lower())

print(autores)
"""

