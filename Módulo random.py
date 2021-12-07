"""
Módulo Random e o que são módulos?

- Em Python, módulos nada mais são do que arquivos Python.

Módulo Random -> Possui várias funções para geração de números pseudo-aleatórios (POIS OS VALORES PODEM SE REPETIR).

# OBS: Existem duas formas de se utilizar um módulo ou função deste

# Forma 1 - Importando todo o módulo (Não recomendado).

import random

# random() -> Gera um número REAL pseudo-aleatório entre 0 e 1.

# Ao realizar o import de todo o módulo, todas as funções, atributos, classes e propriedades que estiverem
# dentro do módulo ficarão disponíveis (Ficarão em memória). Caso você saiba quais funções você precisa utilizar
# deste módulo, então esta não seria a forma ideal de utilização.

print(random.random())

# Veja que para utilizazr a função random() do pacote random, nós colocamos o nome do pacotte e o nome da função
# separados por ponto.

# OBS: Não confunda a função random() copm o pacote random. Pode parecer confuso, mas a função random() é
# apenas uma função dentro do módulo random.

# Forma 2 - Importando uma função específica do módulo

from random import random

#   No import acima, estamos falando: Do módulo random, importe a função random

from random import random

for c in range(10):
    print(random())

# uniform -> Gerar um número REAL pseudo-aleatório entre os valores estabelecidos.

from random import uniform

for i in range(0, 1):
    print(uniform(3, 7))   # 7 NÃO É INCLUÍDO.

# randint() -> Gera valores INTEIROS pseudo-aleatórios entre os valores estabelecidos.
from random import randint

# Gerador de apostas para a mega-sena
for i in range(6):
    print(randint(1, 61), end=', ')     # Começa em 1 e vai até 60

# choice() -> Mostra um valor aleatório entre um iterável.
from random import choice

jogadas = ['pedra', 'papel', 'tesoura']

print(choice('Geek University'))

# shuffle() -> Tem a função de embaralhar dados

from random import shuffle

cartas = ['K', 'Q', 'J', 'A', '2', '3', '4', '5', '6', '7']

print(cartas)

shuffle(cartas)

print(cartas)

"""

