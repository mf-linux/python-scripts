# exer_34.py

# Descrição
#   Deletando variáveis e listas

# Versão 1.0

# Author: Marcus Fermino

# GitHub: https://www.github.com/mf-linux

pares, impares = [], []

limite = int(input('A contagem deve ser feita até qual valor: '))

for i in range(1, limite + 1):
    if i % 2 == 0: pares.append(i) 
    else: impares.append(i)

numeros = (pares, impares)
del pares, impares

print(f'Pares: {numeros[0]}', f'Impares: {numeros[1]}', sep='\n')

