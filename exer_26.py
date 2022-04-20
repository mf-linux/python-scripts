# exer_26.py

# Descrição
#   Usando funções com xargs

# Versão 1.0

# Author: Marcus Fermino

# GitHub: https://www.github.com/mf-linux

# Funções
def somatorio(*x):
    sum = 0
    for arg in x:
        sum += arg
    return sum

def produtorio(*x):
    prod = 1
    for arg in x:
        prod *= arg
    return prod


# Execução
amarelo = '\033[1;33m'
vermelho = '\033[1;31m'
padrao = '\033[0;0m'

print(amarelo, '\u03a3:', padrao, ' ', somatorio(2, 4, 8, 16), sep='')
print(vermelho, '\u03a0:', padrao, ' ', produtorio(2, 4, 8, 16), sep='')
