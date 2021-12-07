"""
Erros mais comuns em Python

ATENÇÃO: É importante prestar atenção e aprender a ler as saídas de erros geradas pela execução.

Os erros mais comuns:

SyntaxError -> Ocorre quando o Python encontra um erro de sintaxe. Ou seja, você escreveu algo que o Python
não reconhece como parte da linguagem.

Exemplos SyntaxError

# 1

def funcao:
    print('Geek')

# 2

None = 1

# 3

return

NameError -> Ocorre quando uma variável ou função não foi definida.

# Exemplos NameError

# 1

print(para_aula_pacotes)

# 2

para_aula_pacotes()

# 3

a = 18

if a < 10:
    msg = 'É maior que 10'
print(msg)

TypeError -> Ocorre quando uma função/operação/ação é aplicada a um tipo errado.

Exemplos TypeError:

# 1

print(len(5))

# 2

print('Geek' + [])

IndexError -> Ocorre quando tentamos acessar um elemento em uma lista ou outro tipo de dado indexado
utilizando um índice inválido.

# Exemplos IndexError

# 1

lista = ['Geek']
print(lista[2])

# 2

lista = ['Geek']
print(lista[0][10])

ValueError -> Ocorre quando uma função ou cooperação built-in recebe um argumento do tipo correto mas
valor inapropriado.

Exemplos ValueError:

# 1

print(int('Geek'))

# 2

print(float('Geek'))

KeyError -> Ocorre quando tentamos acessar um dicionário com uma chave que não existe.

Exemplos KeyError:

# 1

dicio = {}
print(dicio['Geek'])

AttributeError -> Ocorre quando uma variável não tem um atributo ou função.

Exemplos AttributeError:

# 1

tupla = (11, 2, 31, 4)
print(tupla.sort())

IndentationError -> Ocorre quando não respeitamos a indentação do Python, que é de 4 espaços.

Exemplos IndentationError

# 1

def nova():
print('Geek')

# 2

for i in range(10):
i + 1

OBS: Exceptions e Erros são sinônimos na programação.

OBS: Importante ler e prestar atenção na saída de erro.
"""
