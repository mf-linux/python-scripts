# exer_18.py

# Descrição
#    Constroi um retangulo ou quadrado usando for

# Versão 1.0

# Author: Marcus Fermino

# GitHub: https://www.github.com/mf-linux

b = int(input('Informe a base: '))
h = int(input('Informe a altura: '))
caractere = input('Informe o caractere para o desenho: ')

print()

for linhas in range(h):
    for colunas in range(b):
        print(f'{caractere}', end=' ')
    print()

print()