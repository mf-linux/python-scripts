# exer_10.py

# Descrição
#   Verifica se o usuário é maior ou menor de idade

# Versão 1.0

# Author: Marcus Fermino

# GitHub: https://www.github.com/mf-linux

idade = int(input('Informe a sua idade: '))


if  idade >= 18:
    msg = 'Você é maior de idade.'
else:
    msg = 'Você é menor de idade. '
    if idade >= 16:
        msg += 'Mas você já pode votar, regularize seu título.'


print(msg)

