"""
Unittest - Antes e ap�s hooks

hooks - s�o os testes em si. Ou seja, a execu��o dos testes.

setup() -> � executado antes de cada m�todo de teste. � �til para criarmos inst�ncias de objetos e outros dados;

tearDown() -> � executado ao final de cada m�todo de teste. � �til para excluir dados ou fechar conex�es cmo bancos de dados.


"""

import unittest


class ModuloTest(unittest.TestCase):

    def setUp(self):
        # Configura��es do setUp()
        pass

    def test_primeiro(self):
        # setUp vai rodar antes do teste
        # tearDown() vai rodar ap�s o teste.
        pass

    def test_segundo(self):
        # setUp vai rodar antes do teste
        # tearDown() vai rodar ap�s o teste.
        pass

    def tearDown(self):
        # Confirgura��es do tearDown()
        pass