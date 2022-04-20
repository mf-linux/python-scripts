# exer_25.py

# Descrição
#   Usando funções com retorno

# Versão 1.0

# Author: Marcus Fermino

# GitHub: https://www.github.com/mf-linux

# Função
def media(a, b, c, d):
    somatorio = a + b + c + d
    return somatorio / 4

# Execução
a = float(input('Informe a primeira nota: '))
b = float(input('Informe a segunda nota: '))
c = float(input('Informe a terceira nota: '))
d = float(input('Informe a quarta nota: '))

resultado = media(a, b, c, d)

situacao = 'Aprovado' if resultado >= 6 else 'Recuperação' if  4 <= resultado < 6 else 'Reprovado' 

print('Media:', resultado)
print('Situação:', situacao)