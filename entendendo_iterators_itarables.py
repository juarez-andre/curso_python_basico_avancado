# -*- encoding: utf-8 -*-
"""
Entendendo Iterators e Iterables

Iterator ->
    -Um objeto que pode ser iterado
    -Um objeto que retorna um dado, sendo um elemento por vez quando uma função next() é chamado.

Iterables ->
    - Um objeto que irá retornar um iterator quando a função iter() for chamada.

nome = 'Geek'   # É um iterable mas não é um iterator.
numeros = [1, 2, 3, 4, 5, 6]    # É um iterable mas não é um iterator

print(next(nome))   #TypeError
print(next(numeros))    # TypeError

print(next(it1))    # G
print(next(it1))    # e
print(next(it1))    # e
print(next(it1))    # k
print(next(it1))    # StopIteration

print(next(it2))    # 1
print(next(it2))    # 2
print(next(it2))    # 3
print(next(it2))    # 4
print(next(it2))    # 5
print(next(it2))    # 6
print(next(it2))    # StopIteration

for letra in nome:  # Aqui é aplicada a função iter()
    print(f'{letra}')   # Aqui é chamada a função next() por baixo dos panos.
"""







