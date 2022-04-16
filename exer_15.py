# exer_15.py

# Descrição
#    Percorre uma String com o for deixando letras impares maiúsculas

# Versão 1.0

# Author: Marcus Fermino

# GitHub: https://www.github.com/mf-linux

msg = input('Digite sua mensagem: ')

contador = 0

for letra in msg:
    saida = letra.lower() if contador % 2 == 0 else letra.upper()
    print(saida, end='')
    contador += 1
print('')