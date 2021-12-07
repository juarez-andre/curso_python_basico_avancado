# -*- encoding: utf-8 -*-
"""
JSON E Pickle

JSON -> JavaScript Object Notation

API -> São meios de comunicação entre os serviços oferecidos por empresas (Twitter, Facebook, YouTube...) e
terceiros (nós desenvolvedores).

ret = json.dumps(['produto', {'Playstation 4': ('2TB', 'Novo', '220V', 2340)}])

print(type(ret))

print(ret)


class Gato:

    def __init__(self, nome, raca):
        self.__nome = nome
        self.__raca = raca

    @property
    def nome(self):
        return self.__nome

    @property
    def raca(self):
        return self.__raca

felix = Gato('Felix', 'Vira-Lata')

print(felix.__dict__)

ret = json.dumps(felix.__dict__)

print(ret)      # {'_Gato__nome': 'Felix', '_Gato__raca': 'Vira-Lata'}
                  {"_Gato__nome": "Felix", "_Gato__raca": "Vira-Lata"}

Integrando o JSON com Pickle

pip install jsonpickle

import jsonpickle


class Gato:

    def __init__(self, nome, raca):
        self.__nome = nome
        self.__raca = raca

    @property
    def nome(self):
        return self.__nome

    @property
    def raca(self):
        return self.__raca

felix = Gato('Felix', 'Vira-Lata')

print(felix.__dict__)

ret = json.jsonpickle.encode(felix)

print(ret)  # {"py/object": "__main__.Gato", "_Gato__nome": "Felix", "_Gato__raca": "Vira-Lata"}

# Escrevendo o arquivo json/pickle

import jsonpickle


class Gato:

    def __init__(self, nome, raca):
        self.__nome = nome
        self.__raca = raca

    @property
    def nome(self):
        return self.__nome

    @property
    def raca(self):
        return self.__raca

felix = Gato('Felix', 'Vira-Lata')

with open('felix.json', 'w') as arquivo:
    ret = jsonpickle.encode(felix)
    arquivo.write(ret)


# Lendo o arquivo json/pickle

import jsonpickle


class Gato:

    def __init__(self, nome, raca):
        self.__nome = nome
        self.__raca = raca

    @property
    def nome(self):
        return self.__nome

    @property
    def raca(self):
        return self.__raca


with open('felix.json', 'r') as arquivo:
    conteudo = arquivo.read()
    ret = jsonpickle.decode(conteudo)
    print(ret)
    print(type(ret))
    print(ret.nome)
    print(ret.raca)
"""
