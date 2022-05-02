# exer_48.py

# Descrição
#   Try, Else, Except e Finally

# Versão 1.0

# Author: Marcus Fermino

# GitHub: https://www.github.com/mf-linux

print('Faça quantas divisões quiser')

while True:
    try:
        a = float(input('a: '))
        b = float(input('b: '))
        r = a / b
    except ZeroDivisionError:
        print('\nImpossível dividir por zero')
    else:
        print('\nResultado', r, sep=': ')
    finally:
        c = input('\nDeseja continuar? ')
        if c.upper() != 'S': break 
        print()
    