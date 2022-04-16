# exer_16.py

# Descrição
#    Constrói uma pirâmide usando nested loops

# Versão 1.0

# Author: Marcus Fermino

# GitHub: https://www.github.com/mf-linux

inicio = 5
fim = 0

for x in range(inicio, fim, -1):                # cuida do primeiro elemento de cada linha
    print(' ' * x, 1, sep='', end='')
    for y in range(inicio - x):                 # cuida dos elementos subsequentes
        print(' ', 1, sep='', end='')
    print('')




