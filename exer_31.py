# exer_31.py

# Descrição
#   Condições percorrendo a lista

# Versão 1.0

# Author: Marcus Fermino

# GitHub: https://www.github.com/mf-linux

# Cria uma lista e inicializa ela com valores de 1 a 1000
valores = []
valores.extend(range(1,1001))


while True:
    a = int(input('Informe o valor que deseja procurar? Informe \'-1\' para sair: '))
    
    if a in valores: resposta = 'Valor encontrado'
    elif a == -1: break
    else: resposta = 'Valor não encontrado'
    
    print(resposta)