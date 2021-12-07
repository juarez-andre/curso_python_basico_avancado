"""
Sorted

OBS: Não confunda com a função sort() que já estudamos em listas. O sort() só funciona em listas.
Enquanto o sort() ALTERA a estrutura de uma lista, o sorted() GERA uma nova lista.

Podemos utilizar o sorted() com qualquer iterável.

Como o próprio nome diz, sorted() serve para ordenar.

OBS: o sorted() SEMPRE retorna uma LISTA com os elementos do iterável ordenados.

# Exemplo

numeros = (0, 1, 8, 2)
print(numeros)

print(sorted(numeros))      # Ordenar do menor para o maior

print(numeros)

numeros = (0, 1, 8, 2)
print(numeros)

# Adicionando parâmetros ao sorted()

print(sorted(numeros, reverse=True))

print(tuple(sorted(numeros, reverse=True)))

# Podemos utilizar o sorted() para coisas mais complexas

usuarios = [{'username': 'samuel', 'tweets': ['Eu adoro bolos', 'Eu adoro pizzas']},
            {'username': 'carla', 'tweets': ['Eu adoro carne', 'Eu adoro pizzas']},
            {'username': 'jeff', 'tweets': ['Eu adoro maconha']},
            {'username': 'joão', 'tweets': []}]

print(usuarios)

# Ordenando por username - Ordem alfabética

print(sorted(usuarios, key=lambda x: x['username']))

# Ordenando pelo número de tweets

print(sorted(usuarios, key=lambda x: len(x['tweets'])))
# Último exemplo

musicas = [{"título": "Thunderstruck", "tocou": 3},
           {"título": "Dead Skin Mask", "tocou": 2},
           {"título": "Back in Black", "tocou": 4},
           {"título": "Too old to Rock 'n Roll, Too Young To Die", "tocou": 32}]

# Ordena da menos tocada a mais tocada
print(sorted(musicas, key=lambda musica: musica['tocou']))

# Ordena da mais tocada a menos tocada
print(sorted(musicas, key=lambda musica: musica['tocou'], reverse=True))
"""
