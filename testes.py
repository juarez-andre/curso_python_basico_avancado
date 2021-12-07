# -*- encoding: utf-8 -*-
# Pra aula de intro_unittest
import unittest
from atividades import comer, dormir, eh_engracada


class AtividadesTestes(unittest.TestCase):

    def teste_comer(self):
        """Testando o retorno com comida saudável"""
        self.assertEqual(
            comer('quiabo', True),
            'Estou comendo quiabo pois quero entrar em forma'
        )

    def test_comer_gostosa(self):
        """Testando o retorno com comida gostosa"""
        self.assertEqual(
            comer(comida='pizza', eh_saudavel=False),
            'Estou comendo pizza porque a gente só vive uma vez.'
        )

    def test_dormir_pouco(self):
        """Testando o retorno dormindo pouco"""
        self.assertEqual(
            dormir(4),
            'Continuo cansado após dormir por 4 horas. :('
        )

    def test_dormir_muito(self):
        """Testando o retorno dormindo muito"""
        self.assertEqual(
            dormir(4),
            'Dormi demais e esto atrasado'
        )

    def test_eh_engracada(self):
        # self.assertEqual(eh_engracada('Sergio Malandro'), False)
        self.assertFalse(eh_engracada('Sergio Malandro'))
        self.assertTrue(eh_engracada('Jim Carrey'), 'Jim Carrey deveria ser engraçado')


if __name__ == '__main__':
    unittest.main()

