# exer_19.py

# Descrição
#    Verifica a situação da média de um aluno usando for e else

# Versão 1.0

# Author: Marcus Fermino

# GitHub: https://www.github.com/mf-linux

print('Informe suas notas, use valores de 0 a 10', end='\n\n')

notas = [
    float(input('Primeira nota: ')),
    float(input('Segunda nota: ')),
    float(input('Terceira nota: ')),
    float(input('Quarta nota: '))
]

media = 0
msg = 'Sua media é {} e você está {} !'

for i in range(4):
    media += notas[i]
    if media >= 20: 
        msg = msg.format(media, 'aprovado')
        break
else:
    msg = msg.format(media,'reprovado')


print('\nSituação', msg, sep=': ')