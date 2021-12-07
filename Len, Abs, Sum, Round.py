"""
Len, Abs, Sum, Round

# Len

len() -> Retorna o número de itens de um iterável.

# Por debaixo dos panos, quando utilizamos o função len() o Python faz o seguinte:

# Dunder len

print('Geek University'.__len__())

# Abs

abs() -> Retorna o valor absoluto de um número  inteiro ou real. De forma básica seria seu valor real
sem o sinal.

# Exemplos Abs

print(abs(-5))  # 5
print(abs(5))   # 5
print(abs(3.14))    # 3.14
print(abs(-3.14))   # 3.14

print(abs('para_aula_pacotes'))  # TypeError

# Sum

sum() -> Recebe como parâmetro um iterável podendo receber um valor inicial, e retorna a soma tootal dos
elementos, incluindo o valor inicial.

OBS: O valor inicial default é 0

# Exemplos Sum

print(sum([1, 2, 3, 4, 5]))     # 15

print(sum([1, 2, 3, 4, 5], 5))      # 20

print(sum([3.145, 5.678]))      # 8.823

print(sum((1, 2, 3, 4, 5)))     # 15

print(sum({1, 2, 3, 4, 5}))     # 15

print(sum({'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}.values()))     # 15

OBS: sum() não funciona com strings

# Round

round() -> Retorna um número arredondado para n digitos de precisão após a casa decimal. Se a precisão não
for informada retorna o inteiro mais próximo da entrada.
"""
# Exemplos Round

print(round(10.2))      # 10

print(round(10.5))      # 10

print(round(10.6))      # 11

print(round(1.21212121, 2))     # 1.21

print(round(1.21999999, 2))     # 1.22