# exer_50.py

# Descrição
#   Múltiplos Exceções em um único tratador

# Versão 1.0

# Author: Marcus Fermino

# GitHub: https://www.github.com/mf-linux

raiz_n = lambda x, n: x ** (1 / n)

try:
    x = float(input('x: '))
    n = float(input('n: '))
    r = raiz_n(x, n)
except (ZeroDivisionError, ValueError):
    print('\033[1;31m x\033[0;0m deve ser um número real e\033[1;31m n\033[0;0m deve ser um real não nulo')
else:
    print(f'{n}\u221a{x} = {r}')
