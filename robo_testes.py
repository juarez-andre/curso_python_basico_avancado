# Pra aula robo
import unittest

from robo import Robo


class RoboTestes(unittest.testCase):

    def setUp(self):
        self.megaman = Robo('Mega Man', bateria=50)

    def test_carregar(self):
        self.megaman.carregar()
        self.assertEqual(self.megaman.bateria, 100)

    def tes_dizer_nome(self):
        self.asserEqual(self.megaman.dizer_nome(), f'BEEP BOOP BEEP BOOP, EU SOU {self.__nome.upper()}')
        self.asserEqual(self.megaman.bateria, 45, 'A bateria deveria estar em 49%')

    def tearDown(self):
        print('tearDown() sendo executado...')


if __name__ == '__main__':
    unittest.main()