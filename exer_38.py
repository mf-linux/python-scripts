# exer_38.py

# Descrição
#   Manipulação de dicionários

# Versão 1.0

# Author: Marcus Fermino

# GitHub: https://www.github.com/mf-linux

def media(notas):
    somatorio = 0
    for n in notas:
        somatorio += int(n)
    return somatorio / len(notas)


alunos = {}

while True:
    a_tmp = input('Informe o nome do aluno: ')
    
    n_tmp = input('Informe as notas desse aluno separadas por virgula e sem espaço: ')
    n_tmp = tuple(n_tmp.split(','))

    alunos.update({a_tmp: n_tmp})

    r = input('\nDeseja continuar s/N? ')
    
    if r != 's' and r != 'S': break
    
    print('')

print('\nAluno: Notas', end='\n\n')

for k, v in alunos.items():
    print(k, v, sep=': ', end=' ')
    print('Media', media(v), sep=': ')



