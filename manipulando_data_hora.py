# -*- encoding: utf-8 -*-
"""
Manipulando data e hora

Python tem um módulo built-in para se trabalhar com data e hora chamado datetime.

2018-12-21 15:36:38.056382

2018-12-21 15:41:0.0

import datetime

print(datetime.MAXYEAR)     # 9999

print(datetime.MINYEAR)     # 9999

# Retorna a data e hora corrente

print(datetime.datetime.now())      # 2021-11-16 13:56:18.539274


# datetime.datetime(year, month, day, hour, minute, second, microsecond)

print(repr(datetime.datetime.now()))        # datetime.datetime(2021, 11, 16, 13, 59, 28, 152355)

# replace() para fazer ajustes na data/hora

inicio = datetime.datetime.now()

print(inicio)       # 2021-11-16 13:59:28.153355

# Alterar o horário para 15 horas, 0 minuto, 0 segundo, 0 microsegundo

inicio = inicio.replace(hour=15, minute=0, second=0, microsecond=0)

print(inicio)       # 2021-11-16 15:00:00

# Recebendo dados do usuário e convertendo para data

nascimento = input('Informe sua data de nascimento (dd/mm/yyy) : ')

nascimento = nascimento.split('/')

nascimento = datetime.datetime(int(nascimento[2]), int(nascimento[1]), int(nascimento[0]))

print(type(nascimento))     # <class 'datetime.datetime'>

evento = datetime.datetime.now()

# Acesso individual dos elementos de date e hora

print(evento.year)
print(evento.month)
print(evento.day)
print(evento.hour)
print(evento.minute)
print(evento.second)
print(evento.microsecond)

print(dir(evento))
"""

