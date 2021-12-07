# -*- encoding: utf-8 -*-
"""
Métodos de Data e Hora

# Com now() podemos especificar um timezone (Fuso Horário)
agora = datetime.datetime.now()     # now ==  agora
print(agora)
print(type(agora))
print(repr(agora))


hoje = datetime.datetime.today()    # today == hoje
print(hoje)
print(type(hoje))
print(repr(hoje))

# Mudanças ocorrendo à meia-noite combine()

manutencao = datetime.datetime.combine((datetime.datetime.now() + datetime.timedelta(days=1)), datetime.time())

print(manutencao)
print(type(manutencao))
print(repr(manutencao))

# Encontrar o dia da semana, weekday()

# Os dias da semana do método weekday() começam em 0, sendo esta a segunda-feira

# 0 - Segunda-feira (Monday)
# 1 - Terça-feira (Tuesday)
# 2 - Quarta-feira (Wednesday)
# 3 - Quinta-feira (Thursday)
# 4 - Sexta-feira (Friday)
# 5 - Sábado-feira (Saturday)
# 6 - Domingo (Sunday)

manutencao = datetime.datetime.combine((datetime.datetime.now() + datetime.timedelta(days=1)), datetime.time())

print(manutencao.weekday())

# Formatando data/horas com strftime() (String Format Time)
# dd/mm/yyyy hora:minuto

hoje = datetime.datetime.today()
print(hoje)

hoje_formatado = hoje.strftime('%d/%m/%y')

print(hoje_formatado)

from textblob import TextBlob


def formata_data(data):
    return f"{data.day} de {TextBlob(data.strftime('%B')).translate(to='pt-br')} de {data.year}"

hoje = datetime.datetime.today()

print(formata_data(hoje))

nascimento = datetime.datetime.strptime('10/04/1988', '%d/%m/%Y')

print(nascimento)

nascimento = input('Qual sua data de nascimento? (dd/mm/yyyy): ')

nascimento = datetime.datetime.strptime(nascimento, '%d/%m/%Y')

print(nascimento)

# Somente a hora

almoco = datetime.time(12, 30, 0)

print(almoco)

import timeit

# Marcando tempo de execução do nosso código com timeit

# Loop for
tempo = timeit.timeit('"-".join(str(n) for n in range(100))', number=10000)
print(tempo)

# List Comprehension
tempo = timeit.timeit('"-".join([str(n) for n in range(100)])', number=10000)
print(tempo)

# Map
tempo = timeit.timeit('"-".join(map(str, range(100)))', number=10000)
print(tempo)

import timeit, functools


def teste(n):
    soma = 0
    for num in range(n * 200):
        soma = soma + num + 4
    return soma


print(timeit.timeit(functools.partial(teste, 2), number=100000))
"""

