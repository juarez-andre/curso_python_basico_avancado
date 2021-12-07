# -*- encoding: utf-8 -*-
"""
Programação Orientada a Objeto - POO

- POO é um paradigma de programação que utiliza que utiliza mapeamento de objetos do mundo real para modelos
computacionais.

- Paradigma de programação é a forma/metodologia utilizada para pensar/desenvolver sistemas.

Principais elementos da Orientação a Objetos
- Classe -> Modelo do objeto do mundo real sendo representado computacionalmente;
- Atributo -> Características do objeto;
- Método -> Comportamento do objeto (funções);
- Construtor -> Método especial utilizado para criar os objetos;
- Objeto -> Instância de classe.

numero = 10
print(numero)
print(type(numero))

nome = 'Geek'
print(nome)     # <__main__.Produto object at 0x00000263A09ED550> - ISSO ESTÁ REFERENCIANDO UM ENDEREÇO DE MEMÓRIA
print(type(nome))       # <class '__main__.Produto'> - Classe: Produto


class Produto:
    pass


ps4 = Produto()
print(ps4)
print(type(ps4))
"""
