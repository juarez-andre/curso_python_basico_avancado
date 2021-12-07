"""
Lendo arquivos CSV

CSV - Comma Separeted Values - Valores Separados por V�rgula

# Separado por v�rgula

1, 2, 3, 4, 5, 6

"geek", "university", "python", "ci�ncia", "dados"

# Separado por ponto e v�rgula

1; 2; 3; 4; 5; 6

"geek"; "university"; "python"; "ci�ncia"; "dados"

# Sepadador por espa�o

1 2 3 4 5 6

"geek" "university" "python" "ci�ncia" "dados"

http://dados.gov.br/dataset

# Poss�vel de se trabalhar, mas n�o � o ideal (trabalhoso)

with open('lutadores.csv') as arquivo:
    dados = arquivo.read()
    # print(type(dados))
    dados = dados.split(',')[2:]
    print(dados)


A linguagem Python possui duas formas diferentes para ler dados em arquivos CSV:
    - reader -> Permite que iteremos sobre as linhas do arquivo CSV como listas;
    - DictReader -> Permite que iteremos sobre as linhas do arquivo CSV como OrderedDicts;

# Reader

from csv import reader


with open('lutadores.txt') as arquivo:
    leitor_csv = reader(arquivo)
    next(leitor_csv)    # Pular o cabe�alho
    for linha in leitor_csv:
        # Cada linha � uma lista
        print(f' {linha[0]} nasceu no(a)(s) {linha[1]} e mede {linha[2]} cent�metros')

# DictReader

from csv import DictReader

with open('lutadores.csv') as arquivo:
    leitor_csv = DictReader(arquivo)
    for linha in leitor_csv:
        # Cada linha � um OrderedDict
        print('{linha['Nome']} nasceu no(a)(s) {linha['Pa�s'] e mede {linha['Altura (em cm)']}")
"""