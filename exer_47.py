# exer_47.py

# Descrição
#   Try e Except

# Versão 1.0

# Author: Marcus Fermino

# GitHub: https://www.github.com/mf-linux


try:
    a = float(input('a: '))
    b = float(input('b: '))
    r = a / b
    print(r)
except ZeroDivisionError:
    print('Erro não é possível dividir por zero')
    