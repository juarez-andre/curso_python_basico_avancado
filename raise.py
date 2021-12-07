"""
Levantando erros com raise

raise -> Lança exceções

OBS: O raise não é uma função. É uma palavra reservada, assim como def ou qualquer outro em Python.

Para simplificar, pense no raise como sendo util para que possamos criar nossas próprias exceções e mensagens.

A forma geral de utilização é:

rase TipoDoErro('Mensagem de erro')

# Exemplo real

def colore(texto, cor):
    cores = ('verde', 'amarelo', 'azul', 'branco')
    if cor not in cores:
        raise ValueError(f'A cor precisa ser uma entre {cores}')
    if type(texto) is not str:
        raise TypeError('texto precisa ser uma string')
    if type(cor) is not str:
        raise TypeError('cor precisa ser uma string')
    print(f'O texto {texto} será impresso na cor {cor}')

colore('Geek', 'verde')

OBS: o raise, assim como o return, finaliza a função. Ou seja, nada após o raise será executado
"""
