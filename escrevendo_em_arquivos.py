"""
Escrevendo em Arquivos

# OBS: Ao abrir um arquivo para leitura, não podemos realizar a escrita nele (apenas ler). E vice-versa

# Ao abrir um arquivo para escrita, o arquivo é criado no sistema operacional.

Para escrevermos em um arquivo, após abrir o arquivo utilizamos a função write().
Esta função recebe uma string como parâmetro.

Abrindo um arquivo para escrita com o modo 'w', se o arquivo não existir, será criado. Caso contrário, o anterior
será apagado e um novo será criado. Dessa forma todo o conteúdo do arquivo anterior é PERDIDO.

# Exemplo de escrita - modo 'w' = write (escrita)

with open('novo.txt', 'w') as arquivo:
    arquivo.write('Escrever dasdos em arquivos é muito fácil.\n')
    arquivo.write('Podemos colocar quantas linhas quisermos.\n')
    arquivo.write('Esta é a última linha.')
    arquivo.write(42)   # TypeError - PRECISA SER STRING

É bom lembrar que o modo de abertura padrão da função open() é pra LEITURA. Já que nesse caso queremos abrir
no modo ESCRITA, devemos passar o 'w'.

Recebendo dados do usuário:

with open('frutas.txt', 'w', encoding='utf=8') as arquivo:
    while True:
        fruta = str(input('Digite uma fruta ou digite sair: '))
        if fruta == 'sair':
            break
        arquivo.write(fruta)
        arquivo.write('\n')
"""

