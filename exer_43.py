# exer_43.py

# Descrição
#   Demonstração do uso da função filter

# Versão 1.0

# Author: Marcus Fermino

# GitHub: https://www.github.com/mf-linux

print('PAR OU IMPAR', end='\n\n')

numeros = input('Informe a lista de valores separados por virgula que deseja identificar: ')
numeros = tuple(numeros.split(','))
# Remove espaços desnecessários que possam ter ficado no inicio das strings
numeros = tuple(map(lambda x: int(x.strip()), numeros))

# Determina os pares com filter
pares = tuple(filter(lambda x: x % 2 == 0, numeros))
# Usa diferença de conjuntos para determinar os números impares
impares = tuple(set(numeros) - set(pares))

del numeros

print('')

print(f'Pares: {pares}', f'Impares: {impares}', sep='\n', end='\n\n')