"""
Geradores

- Geradores (Generators) s�o Itera��es (Iteradores).

OBS: o contr�rio n�o � verdadeiro. Ou seja, nem todo iterator � um generator.

Outras informa��es:

- Generators podem ser criados com fun��es geradoras;
- Fun��es geradoras utilizam a palavra reservada yield;
- Generators podem ser criados com Express�es Geradoras;

Diferen�as entre Fun��es e Generator Funciona (Fun��es Geradoras)

Fun��es utilizam return e s� retornam uma vez e quando executadas, retornam um valor.

Generator Functions utilizam yield, podem utilizar yield m�ltiplas vezes e quando executada, retorna um generator.

# Exemplo de fun��o Geradora (Generator Function)

def conta_ate(valor_maximo):
    contador = 1
    while contador <= valor_maximo:
        yield contador
        contador = contador + 1

# OBS: uma Generator Function n�o � um Generator. Ela gera um generator.

gen = conta_ate(10)

print(next(gen))    # 1

print('Geek')

for num in gen:
    print(num)
"""