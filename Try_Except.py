"""
O bloco try/except

Utilizamos o bloco try/except para tratar erros que podem ocorrer no nosso código. Previnindo que
o programa pare de funcionar e o usuário receba mensagens de erro inesperadas.

A forma geral mais simples é:

try:
    //execução problemática
except:
    //o que deve ser feito em caso de problema

# Exemplo 1 - Tratando um erro genérico

try:
    para_aula_pacotes()
except:
    print('Deu algum problema')

# Tente executar a função para_aula_pacotes(), caso você encontre erros, imprima a mensagem de erro.

OBS: Tratar erro de forma genérica não é a melhor forma de tratamento de erro. O ideal é SEMPRE tratar
de forma específica.

# Exemplo 2 - Tratando um erro específico

try:
    para_aula_pacotes()
except NameError:
    print('Você está utilizando uma função inexistente')

# Exemplo 3 - Tratando um erro específico

try:
    len(5)
except TypeError as err:
    print(f'A aplicação gerou o seguinte erro: {err}')

# Podemos efetuar diversos tratamentos de erros de uma vez.

try:
    para_aula_pacotes()
except NameError as erra:
    print(f'Deu NameError: {erra}')
except TypeError as errb:
    print(f'Deu TypeError: {errb}')
except:
    print('Deu um erro diferente')


def pegavalor(dicionario, chave):
    try:
        return dicionario[chave]
    except KeyError:
        return None
    except TypeError:
        return None

dic = {'nome': 'Geek'}

print(pegavalor(dic, 'nome'))
"""