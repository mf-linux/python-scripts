# exer_39.py

# Descrição
#   Lambdas

# Versão 1.0

# Author: Marcus Fermino

# GitHub: https://www.github.com/mf-linux

operacoes = {
    1: lambda x, y: x + y,
    2: lambda x, y: x - y,
    3: lambda x, y: x * y,
    4: lambda x, y: x / y,
    'zero_d': lambda x, y: f'Erro a divisão ({x} / {y}) é impossível, contém divisão por zero'
}

print('Informe o número da operação que deseja realizar: ')
print('1 - Soma', '2 - Subtração', '3 - Multiplicação', '4 - Divisão', sep='\n', end='\n\n')
op = int(input(': '))

if op in operacoes.keys():
    x = float(input('\nx : '))
    y = float(input('y: '))
    if op == 4 and y == 0: op = 'zero_d'
    r = operacoes[op](x, y)
else:
    r = 'Erro operação invalida'

print(f'\n{r}')