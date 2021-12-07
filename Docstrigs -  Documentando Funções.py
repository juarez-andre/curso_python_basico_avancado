"""
Documentando funções com Docstrings

OSB: Podemos ter acesso à documentação de uma função em Python utilizando a propriedade __doc__

Podemos ainda fazer acesso a documentação com a função help()

#Exemplos

def diz_oi():
  ""Uma função simples que retorna a string Oi ""
    return 'Oi'


print(diz_oi())
print(help(diz_oi))
print(diz_oi.__doc__)


def exponencial(numero, potencia=2):
    ""Função que retorna como padrão o quadrado de 'numero' ou 'numero' à potência informada.
    :param numero: número que desejamos ver o potencial
    :param potencia: valor da potencia
    :return: retorna o valor do número por potencia
    ""
    return numero ** potencia

print(help(exponencial))
print(exponencial.__doc__)
"""
