# exer_13.py

# Descrição
#   Encontra as raízes de equações quadráticas


# Versão 1.0

# Author: Marcus Fermino

# GitHub: https://www.github.com/mf-linux

a = float(input('Informe o valor de a: '))
b = float(input('Informe o valor de b: '))
c = float(input('Informe o valor de c: '))

raizes = 'x\' = {} ; x\'\' = {}'

x = []

if a != 0 and b != 0 and c != 0:                    # Equação do tipo ax²+bx+c=0
    delta = b ** 2 - 4 * a * c
    x.append(((-b + delta ** 0.5) / 2 * a))
    x.append(((-b - delta ** 0.5) / 2 * a))
elif a != 0 and b != 0 and c == 0:                  # Equação do tipo ax²+b=0
    x.append(0)
    x.append((-b / a))
elif a != 0 and b == 0 and c != 0:                  # Equação do tipo ax²+c=0
    x.append(((-c / a) ** 0.5))
    x.append((x[0] * -1))


print(raizes.format(x[0], x[1]))