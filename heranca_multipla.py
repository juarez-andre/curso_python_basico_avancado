# -*- encoding: utf-8 -*-
"""
POO - Herança múltipla

Herança Múltipla nada mais é do que a possibilidade de uma classe herdar de múltiplas classes, fazendo
com que a classe filha herde todos os atributos e métodos de todas as classes herdadas.

OBS: A herança múltipla pode ser feita de duas maneiras:
    - Por multiderivação direta;
    - Por multiderivação indireta;

# Exemplo - Multiderivação Direta


class Base1:
    pass


class Base2:
    pass


class Base3:
    pass


class Multiderivada(Base1, Base2, Base3):
    pass


# Exemplo 2 - Multiderivação Indireta

class Base1:
    pass


class Base2(Base1):
    pass


class Base3(Base2):
    pass


class Multiderivada(Base3):
    pass

OBS: Não importa se a derivação é direta ou indireta, a classe que realizar a herança herdará todos os atributos
e métodos das super classes.
"""


class Animal:
    def __init__(self, nome):
        self.__nome = nome

    @property
    def nome(self):
        return self._Animal__nome

    @property
    def cumprimentar(self):
        return f'Eu sou {self.__nome}'


class Aquatico(Animal):
    def __init__(self, nome):
        super().__init__(nome)

    @property
    def nadar(self):
        return f'{self._Animal__nome} esta nadando...'

    @property
    def cumprimentar(self):
        return f'Eu sou {self._Animal__nome} do mar!'


class Terrestre(Animal):

    def __init__(self, nome):
        super().__init__(nome)

    @property
    def andar(self):
        return f'{self._Animal__nome} está andando...'

    @property
    def cumprimentar(self):
        return f'Eu sou {self._Animal__nome} da terra!'


class Pinguim(Terrestre, Aquatico):
    def __init__(self, nome):
        super().__init__(nome)

# Testando


baleia = Aquatico('Wally')
print(baleia.nadar)
print(baleia.cumprimentar)

tatu = Terrestre('Xim')
print(tatu.andar)
print(tatu.cumprimentar)

tux = Pinguim("Tux")
print(tux.andar)
print(tux.nadar)
print(tux.cumprimentar)   # Eu sou Tux da terra! (Pois a herança terrestre veio primeiro na construção da classe Pinguim) - Method Resolution Order - MRO

# Objeto é instância de...

print(f"Tux é instância de Pinguim? {isinstance(tux, Pinguim)}")    # True
print(f"Tux é instância de Aquático? {isinstance(tux, Aquatico)}")    # True
print(f"Tux é instância de Terrestre? {isinstance(tux, Terrestre)}")    # True
print(f"Tux é instância de Animal? {isinstance(tux, Animal)}")    # True
print(f"Tux é instância de object? {isinstance(tux, object)}")  # True
# Toda classe em Python herda de object
