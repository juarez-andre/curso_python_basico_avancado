"""
Preservando metadados -> S�o dados intr�nsecos em arquivos.

wraps -> S�o fun��es que envolvem elementos com diversas finalidades.

# Problema

def ver_log(funcao):
    def logar(*args, **kwargs):
        # Eu sou uma fun��o (logar) dentro de outra.
        print(f'Voc� est� chamando {fun��o._name_}')
        print('Aqui a documenta��o: {fun��o._doc_}')
        return funcao(*args, **kwargs)
    retorno logar


@ver_log
def soma(a, b);
    ""Soma dois n�meros""
    return a + b

print(soma(10, 30))

print(soma._name_) # DEVERIA TER: soma
print(soma._doc_) # DEVERIA TER: soma dois n�meros.

# Resolu��o do problema

from functools import wraps

def ver_log(funcao):
    @wraps(funcao)
    def logar(*args, **kwargs):
        #Eu sou uma fun��o (logar) dentro de outra.
        print(f'Voc� est� chamando {fun��o._name_}')
        print('Aqui a documenta��o: {fun��o._doc_}')
        return funcao(*args, **kwargs)
    retorn logar

@ver_log
def soma(a, b):
    #Soma dois n�meros
    return a + b

print(soma(10, 30))

print(soma._name_) # soma
print(soma._doc_) # soma dois n�meros.
"""