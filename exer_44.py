# exer_43.py

# Descrição
#   Números primos usando List Comprehension

# Versão 1.0

# Author: Marcus Fermino

# GitHub: https://www.github.com/mf-linux


a = int(input('\nInforme o valor que deseja descobrir se é primo: '))

# Cria uma lista com os divisores do número desprezando o 1 e ele mesmo
divisores = [x for x in range(2, a) if a % x == 0]

# Verifica o tamanho da lista, se for 0 não há divisores e portanto é primo caso contrário não é
saida = '\nPrimo\n' if len(divisores) == 0 else f'\nNão é primo, seus divisores são\n{divisores}\n'

print(saida)

