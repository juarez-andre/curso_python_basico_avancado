"""
Geradores

- Geradores (Generators) são Iterações (Iteradores).

OBS: o contrário não é verdadeiro. Ou seja, nem todo iterator é um generator.

Outras informações:

- Generators podem ser criados com funções geradoras;
- Funções geradoras utilizam a palavra reservada yield;
- Generators podem ser criados com Expressões Geradoras;

Diferenças entre Funções e Generator Funciona (Funções Geradoras)

Funções utilizam return e só retornam uma vez e quando executadas, retornam um valor.

Generator Functions utilizam yield, podem utilizar yield múltiplas vezes e quando executada, retorna um generator.

# Exemplo de função Geradora (Generator Function)

def conta_ate(valor_maximo):
    contador = 1
    while contador <= valor_maximo:
        yield contador
        contador = contador + 1

# OBS: uma Generator Function não é um Generator. Ela gera um generator.

gen = conta_ate(10)

print(next(gen))    # 1

print('Geek')

for num in gen:
    print(num)
"""