"""
List Comprehension

- Utilizando list comprehension nós podemos gerar novas listas com dados processados a partir de
outro iterável.

# Sintaxe da List Comprehension

[dado for dado in iterável]

numeros = [1, 2, 3, 4, 5]

res = [numero * 10 for numero in numeros]

print(res)

Para entender melhor o que está acontecendo devemos dividir a expressõa em duas partes:

- A primeira parte: for numero in numeros
- A segunda parte: numero * 10

res = [numero / 2 for numero in numeros]
print(res)


def funcao(valor):
    return valor * valor


res = [funcao(numero) for numero in numeros]
print(res)


#List Comprehension vs Loop

# Loop
numeros = [1, 2, 3, 4, 5]

numeros_dobrados = []
for numero in numeros:
    numero_dobrado = numero * 2
    numeros_dobrados.append(numero_dobrado)

print(numeros_dobrados)

# List Comprehension
print([numero * 2 for numero in numeros])


# Outros exemplos

# 1

nome = 'Geek University'

print([letra.upper() for letra in nome])

# 2

amigos = ['maria julia', 'julia', 'pedro']

print([amigo.capitalize() for amigo in amigos])

# 3

print([numero * 3 for numero in range(1, 10)])

# 4

print([bool(valor) for valor in [0, [], '', True, 1, 3.14]])

# 5

print([str(numero) for numero in [1, 2, 3, 4, 5]])


Nós podemos adicionar estruturas condicionais lógicas às nossas List Comprehension

OBS: LEMBRANDO QUE CASO HAJA IF E ELSE, COLOCAR NO INÍCIO. PORÉM SE HAVER APENAS UM IF, COLOCÁ-LO NO FINAL

# Exemplos

# 1

numeros = [1, 2, 3, 4, 5, 6]

pares = [numero for numero in numeros if numero % 2 == 0]
impares = [numero for numero in numeros if numero % 2 != 0]

print(pares)
print(impares)

# Refatorar

# Qualquer número par módulo de 2 é 0, e 0 em Python é False. not False =  True
pares = [numero for numero in numeros if not numero % 2]

# Qualquer número impar módulo de 2 é 1, e 1 e, Python é True.
impares = [numero for numero in numeros if numero % 2]

# 2

res = [numero * 2 if numero % 2 == 0 else numero / 2 for numero in numeros]

print(res)

"""
