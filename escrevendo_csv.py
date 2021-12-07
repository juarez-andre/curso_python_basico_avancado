"""
Escrevendo em arquivos CSV

reader() (leitor), writer() (escritor)

writerow() -> Escreve uma linha

# writer() -> Gera um objeto para que possamos escrever em um arquivo CSV. Utilizamos o m�todo writerow() para escrever cada linha. Este m�dulo recebe uma lista.

from csv import writer

with open('filmes.csv', 'w') as arquivo:
    escritor_csv = writer(arquivo)
    filme = None
    escritor_csv.writerow(['T�tulo', 'G�nero', 'Dura��o'])
    while filme != 'sair':
        filme = input('Informe o nome do filme: ')
        if filme != 'sair':
            genero = input('Informe o g�nero: ')
            duracao = input('Informe a dura��o (em minutos): ')
            escritor_csv.writerow([filme, genero, duracao])

# DictWriter

# OBS: As chaves do dicion�rio devem ser as mesmas utilizadas como cabe�alho

from csv import DictWriter

with open('filmes2.csv', 'w') as arquivo:
    cabe�alho = ['T�tulo', 'G�nero', 'Dura��o']
    escritor_csv = DictWriter(arquivo, fieldnames=cabecalho)
    escritor_csv.writeheader()
    filme = None
    while filme != 'sair':
        filme = input('Informe o nome do filme: ')
        if filme != 'sair':
            genero = input('Informe o g�nero: ')
            duracao = input('Informe a dura��o (em minutos): ')
            escritor_csv.writerow({"T�tulo": filme, "G�nero": genero, "Dura��o": duracao})
"""