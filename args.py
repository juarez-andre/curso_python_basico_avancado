"""
Entendendo o *args
- O *args é um parâmetro, como outro qualquer. Isso significa que vc poderá
 chamar de qualquer coisa, desde que comece com asterisco.

# Exemplo

*xis
Mas por convenção, utilizamos *args para defini-lo

O parâmetro *args utilizado em uma função coloca os valores extras informados como entrada em uma tupla.
Então desde já lembre-se que tuplas são imutáveis.


#Exemplos


def soma_todos_numeros(num1, num2, num3):
    return num1 + num2 + num3

print(soma_todos_numeros(4, 6, 9))

# print(soma_todos_numeros(4, 7))   #   TypeError


# Entendendo o args


def soma_todos_numeros(*args):
    return sum(args)


print(soma_todos_numeros())
print(soma_todos_numeros(1))
print(soma_todos_numeros(3, 4))
print(soma_todos_numeros(3, 4, 5))
print(soma_todos_numeros(1, 2, 3, 4, 5))


# Outro exemplo de utilização do *args

def verifica_info(*args):
    if 'Geek' in args and 'University' in args:
        return 'Bem vindo Geek'
    return 'Não tenho certeza de quem vc é'


print(verifica_info())
print(verifica_info(1, True, 'University', 'Geek'))
print(verifica_info(1, 'University', 3.145))

# DESEMPACOTANDO VÁRIAVEIS COMPOSTAS ATRAVÉS DO ARGS


def soma_todos_numeros(*args):
    return sum(args)


numeros = [1, 2, 3, 4, 5, 6]
print(soma_todos_numeros(numeros))  # TypeError - A lista é adicionada como se fosse um único valor dentro da tupla

# Desempacotador

numeros = [1, 2, 3, 4, 5, 6]
print(soma_todos_numeros(*numeros))

OBS: O asterisco serve para que informemos ao Python que estamos passando como argumento
uma coleção de dados. Desta forma ele saberá que precisará desempacotar os dados
"""
