# exer_29.py

# Descrição
    # Extrai valores da lista para outras variáveis

# Versão 1.0

# Author: Marcus Fermino

# GitHub: https://www.github.com/mf-linux


numeros = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print('Original:', numeros)

# extraindo toda a lista para variáveis
n_0, n_1, *restante = numeros
print(n_0, n_1, 'Restante:', restante)


# extraindo apenas uma parte da lista para outra variávei
numeros[0], numeros[1], *restante = numeros
print('Restante:', restante)

# extraindo apenas uma parte mais ao meio
numeros[0], numeros[1], *restante, numeros[9], numeros[10]  = numeros
print('Restante:', restante)
