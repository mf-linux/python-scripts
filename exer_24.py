# exer_24.py

# Descrição
#   Usando funções com argumentos default e non-default

# Versão 1.0

# Author: Marcus Fermino

# GitHub: https://www.github.com/mf-linux

# Funções
def boas_vindas(nome, msg = 'seja bem vindo(a) !'):
    print('Olá ', nome, ', ', msg, sep='')


# Execução
boas_vindas('Marcus')
boas_vindas('Matheus')
boas_vindas('Wanessa', 'e aí, tudo em cima?')

