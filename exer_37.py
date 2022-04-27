# exer_37.py

# Descrição
#   For percorrendo múltiplas variáveis

# Versão 1.0

# Author: Marcus Fermino

# GitHub: https://www.github.com/mf-linux

nomes, idades = ['Marcus', 'Gabryel', 'Lohran'], [24, 22, 21]

for nome, idade in list(zip(nomes, idades)):
    print(f'Nome: {nome}', f'Idade: {idade}', sep='\n', end='\n\n')