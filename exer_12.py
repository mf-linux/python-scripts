# exer_12.py

# Descrição
#   Demonstra o uso dos statements if, if-else, if-else if-else 
#   de uma única linha.

# Versão 1.0

# Author: Marcus Fermino

# GitHub: https://www.github.com/mf-linux


x = int(input('Digite o valor de x: '))
y = int(input('Digite o valor de y: '))
z = int(input('Digite o valor de z: '))


# if-elif-else cada um ocupando uma linha
if x > y: operador = '>'                                
elif x == y: operador = '='                             
else: operador = '<'                                    

print(x, operador, y)

#if-else ambos ocupando a mesma linha
operador = '>' if x > z else '<='   

print(x, operador, z)

#if-elif-else todos ocupando a mesma linha
operador = '>' if y > z else '=' if y == z else '<'

print(y, operador, z)