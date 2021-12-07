"""
Introdução ao módulo Unittest

Unittest -> Testes Unitários

O que são testes unitários?

Teste é a forma de se testar unidades individuais de código fonte.

Unidades individuais podem ser: funções, métodos, classes, módulos etc.

OBS: Teste unitário não é específico da linguagem Python.

Para criar nossos testes, criamos classes que herdam de unittest. TestCase e a partir de então ganhamos todos
os 'assertions' presentes no módulo.

Para rodar os testes, utiliazamos unittest.main()


TestCase -> Casos de teste para sua unidade.

# Conhecendo as assertions

Método
assertEqual(a, b)   # Checa se a == b
assertNotEqual(a, b)    # Checa se a != b
assertTrue(x)       # Se x é verdadeiro
assertFalse(x)      # Se x é falso
assertIs(a, b)      # a é b
assertIsNot(a, b)   # a não é b
assertIfNone(x)     x é None
assertIfNotNone(x)  # x não é None
assertIn(a, b)      # a está em b
assertNotIn(a, b)   # a não está em b
assertIsInstance(a, b)      # a é instância de b
assertNotInsIstance(a, b)   # a não é instância de b

Por convenção, todos os testes em um test case, devem ter seu nome iniciado com test_

# Para executar os testes com unittest

python nome_do_modulo.py

# Para executar os testes com unittest no modo verbose

python nome_do_modulo -v

# Docstrings nos testes

Podemos acrescentar (e é recomendado_=) docstrings nos nossos testes.

"""