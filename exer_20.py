# exer_20.py

# Descrição
#    Calculadora simples com while

# Versão 1.0

# Author: Marcus Fermino

# GitHub: https://www.github.com/mf-linux

continuar = True

while continuar == True:
    
    x = float(input('Informe o valor de x: '))
    y = float(input('Informe o valor de y: '))

    print('Escolha uma operação', end='\n\n')
    print('-> +', '-> -', '-> *', '-> //', sep='\n', end='\n\n')
    op = input()

    if op == '+': result = '{} + {} = {}'.format(x, y, x + y)
    elif op == '-': result = '{} - {} = {}'.format(x, y, x - y)
    elif op == '*': result = '{} * {} = {}'.format(x, y, x * y)
    elif op == '//': 
        result = 'Divisão por zero não é possível' if y == 0 else '{} // {} = {}'.format(x, y, x // y)
    
    print('\n',result, end='\n\n', sep='')

    questao = input('Deseja continuar? s/N ')

    print()

    if questao == 'N': continuar = False
else:
    print('Você está saindo da calculadora... Adeus!', end='\n\n')