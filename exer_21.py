# exer_21.py

# Descrição
#    Imprime os números impares e pares dentro de um intervalo
#    Colorindo os pares de com uma cor e os impares de com outras

# Versão 1.0

# Author: Marcus Fermino

# GitHub: https://www.github.com/mf-linux


cores = {
    'padrao': '\033[0;0m',
    'preto': '\033[1;30m',
    'vermelho': '\033[1;31m',
    'verde': '\033[1;32m',
    'amarelo': '\033[1;33m',
    'azul': '\033[1;34m',
    'roxo': '\033[1;35m',
    'ciano': '\033[1;36m',
    'branco': '\033[1;37m'
}

limite = int(input('Deseja contar até que número: '))

print()

print('Lista de cores: ', end='')
print('padrao', end=',')
print(cores['preto'], 'preto', cores['padrao'], end=',')
print(cores['vermelho'], 'vermelho', cores['padrao'], end=',')
print(cores['verde'], 'verde', cores['padrao'], end=',')
print(cores['amarelo'], 'amarelo', cores['padrao'], end=',')
print(cores['azul'], 'azul', cores['padrao'], end=',')
print(cores['roxo'], 'roxo', cores['padrao'], end=',')
print(cores['ciano'], 'ciano', cores['padrao'], end=',')
print(cores['branco'], 'branco', cores['padrao'], end='\n\n')

cor_par = input('Qual cor você deseja utilizar para os números pares: ')
cor_impar = input('Qual cor você deseja utilizar para os números impares: ')

print('\nSaida:', end='')

for i in range(1, limite + 1, +1):
    if (i % 2) == 0:                                                  # par?
        print(cores[cor_par], i, cores['padrao'], end='')
    else:         
        print(cores[cor_impar], i, cores['padrao'], end='')           # impar?
print()