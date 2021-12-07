"""
Filter

filter() -> Fltrar dados de uma determinada coleção.

# Biblioteca para trabalhar com dados estatísticos
import statistics

# Dados coletados de algum sensor
dados = [1.3, 2.7, 0.8, 4.1, 4.3, -0.1]

# Calculando a média dos dados utilizando a função mean()

media = statistics.mean(dados)
print(media)

# OBS: Assim como a função map(), a filter() também recebe dois parâmetros, sendo uma função e um iterável

res = filter(lambda x: x > media, dados)
print(list(res))

 # LEMBRANDO QUE DEPOIS QUE EU USO A PRIMEIRA VEZ, ELE NÃO APARECE MAIS. ASSIM COMO NA FUNÇÃO MAP

paises = ['', 'Argentina', '', 'Brasil', 'Chile', '', 'Colômbia', '', 'Equador', '', '', 'Venezuela']

print(list(filter(lambda x: x, paises)))

# A diferença entre Map e Filter é:

# map() -> Recebe dois parâmetros, uma função e um iterável e retorna um objeto mapeando a função para cada elemento de iterável.

# filter() -> Recebe dois parâmetros, uma função e um iterável e retorna um objeto filtrando apenas os elementos de acordo com a função.

# Exemplos mais complexo

usuarios = [{'username': 'samuel', 'tweets': ['Eu adoro bolos', 'Eu adoro pizzas']},
            {'username': 'carla', 'tweets': ['Eu adoro carne', 'Eu adoro pizzas']},
            {'username': 'jeff', 'tweets': ['Eu adoro maconha']},
            {'username': 'joão', 'tweets': []}]

# Filtrar os usuários que estão inativos no Twitter

# Forma 1

print(list(filter(lambda x: not x['tweets'], usuarios)))

# Forma 2

print(list(filter(lambda x: len(x['tweets']) == 0, usuarios)))


# Combinando filter() e map()

nomes = ['Vanessa', 'Ana', 'Maria']

# Devemos criar uma lista contendo 'Sua instrutora é' + nome da instrutora, desde que cada nome tenha menos de 5 caracteres

# Forma 1

print(list(map(lambda x: f'Sua instrutora é {x}', filter(lambda y: len(y) < 5, nomes))))

# Forma 2

print('Sua instrutora é ', end='')
print(list(filter(lambda x: len(x) < 5, nomes)))
"""
