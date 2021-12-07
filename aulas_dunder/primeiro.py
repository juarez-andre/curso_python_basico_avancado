def funcao():
    print('Geek University - primeiro.py')

if __name__=='__main__':
    funcao()
    print('primeiro.py está sendo executado diretamente')
else:
    print(f'primeiro.py foi importado. {__name__}')