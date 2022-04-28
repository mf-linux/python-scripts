# exer_41.py

# Descrição
#   Lambdas dentro de funções

# Versão 1.0

# Author: Marcus Fermino

# GitHub: https://www.github.com/mf-linux

def media(*args):
    somatorio = 0
    for n in args:
        somatorio += n
    return (lambda x, y: x / y) (somatorio, len(args))


print('A média é:', media(10, 10, 3, 4))