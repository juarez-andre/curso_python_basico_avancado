# -*- encoding: utf-8 -*-
"""
POO - Herança (Inheritance)

A ideia de herança é a de reaproveitar código. Também extender nossas classes.

OBS: Com a herança, a partir de uma classe existente, nós extendemos outra classe que passa a herdar atributos
e métodos de classe herdada.

Cliente
    - nome
    - sobrenome
    - cpf
    - renda

Funcionário
    - nome
    - sobrenome
    - cpf
    - matrícula

Existe alguma entidade genérica o suficiente para encapsular os atributos e métodos comuns a outras entidades?


class Cliente:

    def __init__(self, nome, sobrenome, cpf, renda):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__cpf = cpf
        self.__renda = renda

    def nome_completo(self):
        return f'{self.__nome} {self.__sobrenome}'


class Funcionario:

    def __init__(self, nome, sobrenome, cpf, matricula):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__cpf = cpf
        self.__matricula = matricula

    def nome_completo(self):
        return f'{self.__nome} {self.__sobrenome}'


cliente1 = Cliente('Angelina', 'Jolie', '123.456.789.10', 5000)
funcionario1 = Funcionario('Felicity', 'Jones', '987.654.312.00', 1234)

Existe alguma entidade genérica o suficiente para encapsular os atributos e métodos comuns a outras entidades?

OBS: Quando uma classe herda de outra classe ela herda TODOS os atributos e métodos da classe herdada.

Quando uma classe herda de outra classe, a classe herdada é conhecida por:
    [Pessoa]
    - Super Classe;
    - Classe Mãe;
    - Classe Pai;
    - Classe Base;
    - Classe Genérica;

Quando uma classe herda de outra classe, ela é chamada:
    [Cliente, Funcionário]
    - Sub Classe;
    - Classe Filha;
    - Classe Específica;
    

class Pessoa:

    def __init__(self, nome, sobrenome, cpf):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__cpf = cpf

    def nome_completo(self):
        return f'{self.__nome} {self.__sobrenome}'


class Cliente(Pessoa):
    # Cliente herda de pessoa

    def __init__(self, nome, sobrenome, cpf, renda):
        Pessoa.__init__(self, nome, sobrenome, cpf)   # Forma não comum de acessar dados da super classe
        self.__renda = renda


class Funcionario(Pessoa):
    # Funcionario herda de pessoa

    def __init__(self, nome, sobrenome, cpf, matricula):
        super().__init__(nome, sobrenome, cpf)  # Forma comum de acessar dados da super classe.
        self.__matricula = matricula

    def nome_completo(self):
        print(super().nome_completo())
        print(self._Pessoa__cpf)
        return f'Funcionário: {self.__matricula} {self._Pessoa__nome}'


class Penguim(Pessoa):

    def __init__(self, nome, sobrenome):
        self.__nome = nome
        self.__sobrenome = sobrenome


cliente1 = Cliente('Angelina', 'Jolie', '123.456.789.10', 5000)
funcionario1 = Funcionario('Felicity', 'Jones', '987.654.312.00', 1234)

print(cliente1.nome_completo())
print(funcionario1.nome_completo())

print(cliente1.__dict__)

print(funcionario1.__dict__)

# Sobrescrita de Métodos (Overriding)

Sobrescrita de método, ocorre quando reescrevemos/reimplementamos um método presente na super em classes
filhas
"""



