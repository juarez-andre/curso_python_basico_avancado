# -*- encoding: utf-8 -*-
"""
Criando sua própria versão de loop

for num in [1, 2, 3, 4]:    # iter([1, 2, 3, 4])
    print(num)

for letra in 'Geek':    # iter('Geek')
    print(letra)

def meu_for(iteravel):
    it = iter(iteravel)
    while True:
        try:
            print(next(it))
        except StopIteration:
            break

meu_for('Geek University')
"""
