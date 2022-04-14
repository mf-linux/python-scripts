# exer_4.py

# Descrição
#   Descobre a idade aproximada do usuário

# Versão 1.0

# Author: Marcus Fermino

# GitHub: https://www.github.com/mf-linux

anoAtual = int(input('Em que ano estamos? '))
anoNascimento = int(input('Em que ano você nasceu? '))
idade = anoAtual - anoNascimento

print('Sua idade é aproximadamente', idade, sep=': ')
