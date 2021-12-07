"""
Try / Except / Else / Finally

Dica de quando e onde tratar código:

TOODA ENTRADA DEVE SER TRATADA!

OBS: A função do usuário é DESTRUIR seu sistema

Else -> É executadi somente se não ocorrer erro.

try:
    num = int(input('Informe um número: '))
except ValueError:
    print('Valor incorreto')
else:
    print(f'Você digitou {num}')

# Finally

try:
    num = int(input('Informe um número: '))
except ValueError:
    print('Você não digitou um valor válido.')
else:
    print(f'Você digitou o número {num}')
finally:
    print('Executando o finally')

# OBS: O bloco finally é sempre executado independente se houve exceção ou não.

# O finally geralmente é utilizado para fechar ou desalocar recursos.

# Exemplo mais complexo

# Exemplo complexo feito de forma errada:


def dividir(a, b):
    return a / b

try:
    num1 = int(input('Informe o primeiro número: '))
except ValueError:
    print('O valor precisa ser numérico')

try:
    num2 = int(input('Informe o segundo número: '))
except ValueError:
    print('O valor precisa ser numérico')

try:
    print(dividir(num1, num2))
except ValueError:
    print('Só se pode dividir números')

# Exemplo mais complexo CORRETO
# OBS: Você é responsável pelas entradas das suas funções. Então, trate-as!


def dividir(a, b):
    try:
        return int(a) / int(b)
    except ValueError:
        return 'Valor Incorreto'
    except ZeroDivisionError:
        return 'Não é possível realizar uma divisão por 0'


num1 = input('Informe o primeiro número: ')
num2 = input('Informe o segundo número: ')

print(dividir(num1, num2))

# Tratando de forma mais genérica:


def dividir(a, b):
    try:
        return int(a) / int(b)
    except:
        return 'Ocorreu um problema'


num1 = input('Informe o primeiro número: ')
num2 = input('Informe o segundo número: ')

print(dividir(num1, num2))

# Tratando de forma semi-genérica:


def dividir(a, b):
    try:
        return int(a) / int(b)
    except (ValueError, ZeroDivisionError) as err:
        return f'Ocorreu um problema: {err}'


num1 = input('Informe o primeiro número: ')
num2 = input('Informe o segundo número: ')

print(dividir(num1, num2))
"""
