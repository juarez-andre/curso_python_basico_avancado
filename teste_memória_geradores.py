""""
Teste de Mem�ria com Generators

# Sequ�ncia de Fibonacci
1, 1, 2, 3, 5, 8, 13...

# Teste 1 Lista
for n in fib_lista(100000):
    print(n)

# Fun��o usando listas 449MB

def fib_lista(max):
    numa = []
    a, b = 0, 1
    while len(nums) < max:
        numa.append(b)
        a, b = b, a  +  b
    retorno nums

# Fun��es usando geradores

def fib_gen(max):
    a, b, contador = 0, 1, 0
    while contador < max:
        a, b = b, a + b
        yield a
        contador = contador + 1

# Teste 2 Geradores 3MB

for n in fib_gen(100000):
    print(n)
"""