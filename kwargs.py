"""
**kwargs

Poderíamos chamar esse parâmetro de **xis mas por convenção chamamos de **kwargs

Este é só mais um parâmetro, mas diferente do *args que coloca os valores extras em uma tupla, o **kwargs
exige que utilizemos parâmetros nomeados, e transforma esses parâmetros extras em um dicionário.

# Exemplo

def cores_favoritas(**kwargs):
    for pessoa, cor in kwargs.items():
        print(f'A cor favorita de {pessoa.title()} é {cor}')


cores_favoritas(marcos='verde', julia='amarelo', fernanda='azul')

# OBS: Os parâmetros *args e **kwargs não são obrigatórios;

cores_favoritas()
cores_favoritas(para_aula_pacotes='navy')

# Exemplo mais complexo


def cumprimento_especial(**kwargs):
    if 'para_aula_pacotes' in kwargs and kwargs['para_aula_pacotes'] == 'Python':
        return 'você recebeu um cumprimento pythonico'
    elif 'para_aula_pacotes' in kwargs:
        return f"{kwargs['para_aula_pacotes']} Geek"
    return 'Não sei quem tu é'


print(cumprimento_especial())
print(cumprimento_especial(para_aula_pacotes='Python'))
print(cumprimento_especial(para_aula_pacotes='Oi'))
print(cumprimento_especial(para_aula_pacotes='especial'))

# Nas nossas funções, podemos ter (NESTA ORDEM):

- Parâmetros obrigatórios
- *args
- Parâmetros default (não obrigatórios)
- **kwargs


def funcao(idade, nome, *args, solteiro=False, **kwargs):
    print(f'{nome} tem {idade} anos')
    print(args)
    if solteiro:
        print('Solteiro')
    else:
        print('Casado')
    print(kwargs)


funcao(8, 'Julia')
funcao(10, 'Felicity', 4, 5, 3, solteiro=True)
funcao(34, 'Felipe', eu='Não', voce='Vai')
funcao(19, 'Carla', 9, 4, 3, java=False, python=True)

# Entendendo porquê é importante manter a ordem dos parâmetros na declaração

# Função com a ordem correta dos parâmetros:


def mostra_info(a, b, *args, instrutor='Geek', **kwargs):
    return [a, b, args, instrutor, kwargs]


print(mostra_info(1, 2, 3, sobrenome='University', cargo='instrutor'))

# Função com a ordem incorreta de parâmetros:


def mostra_info(a, b, instrutor='Geek', *args, **kwargs):
    return [a, b, args, instrutor, kwargs]


print(mostra_info(1, 2, 3, sobrenome='University', cargo='instrutor'))

# Desempacotar com **kwargs


def mostra_nomes(**kwargs):
    return f"{kwargs['nome']}, {kwargs['sobrenome']}"


nomes = {'nome': 'Felicity', 'sobrenome': 'Jones'}

print(mostra_nomes(**nomes))


def soma_multiplos_numeros(a, b, c):
    print(a + b + c)


lista = [1, 2, 3]
tupla = (1, 2, 3)
conjunto = {1, 2, 3}

soma_multiplos_numeros(*lista)
soma_multiplos_numeros(*tupla)
soma_multiplos_numeros(*conjunto)

dicio = dict(a=1, b=2, c=3)

soma_multiplos_numeros(**dicio)

# OBS: os nomes da chave em um dicionário devem ser o mesmo dos parâmetros da função

dicio = dict(d=1, e=2, f=3)

soma_multiplos_numeros(**dicio)  # TypeError
"""
