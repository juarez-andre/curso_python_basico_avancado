"""
Debugando com PDB

PDB -> Python Debugger

# OBS: A utilização do print() para debugar código é uma prática ruim


def dividir(a, b):
    print(a, b)
    try:
        return int(a) / int(b)
    except (ValueError, ZeroDivisionError) as err:
        return f'Ocorreu um problema: {err}'

print(dividir(4, 7))

# Existem formas mais profissionais de fazer esse "debug", utilizando o debugger
# Em Python, podemos fazer isso em diferentes IDEs, como o PyCharm ou utilizando o PDB.


def dividir(a, b):
    try:
        return int(a) / int(b)
    except (ValueError, ZeroDivisionError) as err:
        return f'Ocorreu um problema: {err}'

print(dividir(1, 1))

# Exemplo com o PDB - Python Debugger

# Para utilizar o Python Debugger, precisamos importar a biblioteca pdb e então utilizar a função set_trace()

# Comandos básicos do PDB
# l (listar onde estamos no código)
# n (próxima linha)
# p (imprime variável)
# c (continua a execução -  finaliza o debugging)

import pdb

nome = 'Angelina'
sobrenome = 'Jolie'
pdb.set_trace()
nome_completo = nome + ' ' + sobrenome
curso = 'Programação em Python Essencial'
final = nome_completo + ' faz o curso ' + curso
print(final)

# Exemplo 2

nome = 'Angelina'
sobrenome = 'Jolie'
import pdb; pdb.set_trace()
nome_completo = nome + ' ' + sobrenome
curso = 'Programação em Python Essencial'
final = nome_completo + ' faz o curso ' + curso
print(final)

# Por que utilizar esse formato?
# O debug é utilizado durante o desenvolvimento. Custumamos realizar todos os imports de bibliotecas
# no início do arquivo. Por isso, ao invés de colocarmos o import do pdb no início do arquivo, nós colocamos
# somente onde vamos debuggar, e ao finalizar já fazemos a remoção.

# Exemplo 3

# A partir do Python 3.7, não é mais necessário importar a biblioteca pdb, pois o comando de debug foi
# incorporado como função built-in (integrada) chamada (breakpoint())

nome = 'Angelina'
sobrenome = 'Jolie'
breakpoint()
nome_completo = nome + ' ' + sobrenome
curso = 'Programação em Python Essencial'
final = nome_completo + ' faz o curso ' + curso
print(final)

# OBS: Cuidado com conflitos entre nomes de variáveis e os comandos do pdb

def soma(l, n, p, c):
    breakpoint()
    return l + n + p + c

print(soma(3, 3, 5, 7))

# Como os nomes das variáveis são os mesmos dos comandos do pdb, devemos utilizar o comando p para imprimir
# as variáveis. Ou seja: p nome_da_variavel

# Mas mesmo assim, nada de colocar nomes não representativos em variáveis. Sempre optar por nomes significativos.
"""

