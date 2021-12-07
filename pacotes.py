"""
Pacotes

Módulo -> É apenas um arquivo Python que pode ter diversas funções para utilizarmos;

Pacote -> É um diretório contendo uma coleção de módulos;   # curso em video é um pacote

OBS: Nas versões 2.x do Python, não é mais obrigatória a utilização deste arquivo, mas normalmente
ainda é utilizado para manter compatibilidade.

from para_aula_pacotes import geek1, geek2

from para_aula_pacotes.university import geek3, geek4

print(geek1.pi)

print(geek1.funcao1(4, 6))

print(geek2.curso)

print(geek2.funcao2())

print(geek3.funcao3())

print(geek4.funcao4())

from para_aula_pacotes.geek1 import funcao1
from para_aula_pacotes.university.geek4 import funcao4

print(funcao1(4, 2))

print(funcao4())
"""
