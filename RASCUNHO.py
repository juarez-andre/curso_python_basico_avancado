# -*- encoding: utf-8 -*-

class Animal:
    def __init__(self, nome, especie, idade):
        self.__nome = nome
        self.__especie = especie
        self.__idade = idade

    @property
    def cumprimentar(self):
        raise NotImplementedError("Você precisa implementar esse método")


class Terrestre(Animal):
    def __init__(self, nome, especie, idade):
        super().__init__(nome, especie, idade)

    @property
    def cumprimentar(self):
        return f"Eu sou o {self._Animal__nome} da terra"


class Aquatico(Animal):
    def __init__(self, nome, especie, idade):
        super().__init__(nome, especie, idade)

    @property
    def cumprimentar(self):
        return f"Eu sou o {self._Animal__nome} da água"


class Pinguim(Terrestre, Aquatico):
    def __init__(self, nome, especie, idade):
        super().__init__(nome, especie, idade)


tux = Pinguim("Tux", "Pinguim", 2)
print(tux.cumprimentar)

rex = Terrestre("Rex", "Cachorro", 7)
print(rex.cumprimentar)

Wally = Aquatico("Wally", "Baleia", 53)
print(Wally.cumprimentar)