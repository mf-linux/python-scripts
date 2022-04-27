# exer_11.py

# Descrição
#   Demonstra o uso dos operadores lógicos

# Versão 1.0

# Author: Marcus Fermino

# GitHub: https://www.github.com/mf-linux

a = True
b = True
c = True

if a == b and b == c:
    print('Todos são iguais')

b = False

if a == b or a == c:
    print('Pelo menos dois são iguais')

if not (a == b):
    print('A e B são diferentes')

if not (a != c):
    print('A e C são iguais')