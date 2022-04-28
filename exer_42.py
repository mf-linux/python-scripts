# exer_42.py

# Descrição
#   Demonstração do uso da função map

# Versão 1.0

# Author: Marcus Fermino

# GitHub: https://www.github.com/mf-linux


def separar(valores):
    return tuple(map(lambda x: float(x.strip()), valores.split(',')))


valores = input('Informe os valores que você deseja descobrir o quadrado: ')
valores = separar(valores)

quad, raiz = lambda x: x ** 2, lambda x: x ** 0.5

print('\nValores:', valores)
print('Quadrados:', tuple(map(quad, valores)))

valores = input('\nInforme os valores que você deseja descobrir as raizes: ')
valores = separar(valores)

print('\nValores:', valores)
print('Raízes:', tuple(map(raiz, valores)))




