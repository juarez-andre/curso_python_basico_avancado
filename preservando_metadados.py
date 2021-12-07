"""
Preservando metadados -> São dados intrínsecos em arquivos.

wraps -> São funções que envolvem elementos com diversas finalidades.

# Problema

def ver_log(funcao):
    def logar(*args, **kwargs):
        # Eu sou uma função (logar) dentro de outra.
        print(f'Você está chamando {função._name_}')
        print('Aqui a documentação: {função._doc_}')
        return funcao(*args, **kwargs)
    retorno logar


@ver_log
def soma(a, b);
    ""Soma dois números""
    return a + b

print(soma(10, 30))

print(soma._name_) # DEVERIA TER: soma
print(soma._doc_) # DEVERIA TER: soma dois números.

# Resolução do problema

from functools import wraps

def ver_log(funcao):
    @wraps(funcao)
    def logar(*args, **kwargs):
        #Eu sou uma função (logar) dentro de outra.
        print(f'Você está chamando {função._name_}')
        print('Aqui a documentação: {função._doc_}')
        return funcao(*args, **kwargs)
    retorn logar

@ver_log
def soma(a, b):
    #Soma dois números
    return a + b

print(soma(10, 30))

print(soma._name_) # soma
print(soma._doc_) # soma dois números.
"""