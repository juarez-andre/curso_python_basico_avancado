# -*- encoding: utf-8 -*-
# Pra aula de intro_unittest
def comer(comida, eh_saudavel):
    if eh_saudavel:
        final = 'quero manter a forma'
    else:
        final = 'a gente só vive uma vez'

    return f'Estou comendo {comida} porque {final}'


def dormir(num_horas):
    if num_horas >8:
        return f'Putz: Dormi muito!'
    else:
        return f'Continuo cansado após dormir por {num_horas} horas. :('


def eh_engracada(pessoa):
    comediantes = ['Jim', 'Bozo']
    if pessoa in comediantes:
        return True
    return False
