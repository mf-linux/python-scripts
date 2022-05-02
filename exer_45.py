# exer_45.py

# Descrição
#   Calculadora utilizando Lambdas, Comprehension, Listas e Dicionários

# Versão 1.0

# Author: Marcus Fermino

# GitHub: https://www.github.com/mf-linux


ops = {
    '1': lambda x, y: x + y,
    '2': lambda x, y: x - y,
    '3': lambda x, y: x * y,
    '4': lambda x, y: x / y,
    '5': lambda x, y = 2: x ** y,
}

print('\nSelecione a operação que deseja realizar', end='\n\n')
print('1 - Soma', '\t\t\tvocê deverá informar as parcelas \'a\' e \'b\'', sep='\n', end='\n\n')
print('2 - Subtração', '\t\t\tvocê deverá informar o minuendo \'a\' e o subtraendo \'b\'', sep='\n', end='\n\n')
print('3 - Multiplicação', '\t\t\tvocê deverá informar os fatores \'a\' e \'b\'', sep='\n', end='\n\n')
print('4 - Divisão', '\t\t\tvocê deverá informar o dividendo \'a\' e o divisor  \'b\'', sep='\n', end='\n\n')
print('5 - Potência', '\t\t\tvocê deverá informar a base \'a\' e o expoente \'b\'', sep='\n', end='\n\n')

op = input(': ')

if op in ops.keys():
    operandos = input('\nInforme os valores a e b para a operação, separados por espaço: ')
    operandos = [ float(n) for n in operandos.split(' ') ]
    
    if op == '4':
        r =  'Erro, divisão por zero' if operandos[1] == 0 else ops[op](operandos[0], operandos[1])
    else:
        r =  ops[op](operandos[0], operandos[1])

print('\nResultado: ', r)


