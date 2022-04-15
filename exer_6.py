# exer_6.py

# Descrição
#   Recebe uma mensagem e a exibe formatada

# Versão 1.0

# Author: Marcus Fermino

# GitHub: https://www.github.com/mf-linux

msg  = input('Insira sua mensagem: ')

print(f'A Mensagem em maísculas: \'{msg.upper()}\'')
print(f'A Mensagem em minúsculas: \'{msg.lower()}\'')
print(f'A Mensagem capitalizada: \'{msg.capitalize()}\'')
print(f'A Mensagem particionada: \'{msg.split()}\'')
print(f'A Mensagem sem espaços em branco antes do primeiro caractere: \'{msg.strip()}\'')
print('A Mensagem com todas as letras A em maísculas: \'%s\'' % msg.replace('a', 'A'))
