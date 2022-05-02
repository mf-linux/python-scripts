# exer_51.py

# Descrição
#   Argumentos de Exceções e Lançamento

# Versão 1.0

# Author: Marcus Fermino

# GitHub: https://www.github.com/mf-linux

def raiz(x):
    if x < 0: raise ValueError(f'Erro, raiz negativa. Não consigo calcular raízes como esta: \'\u221a{x}\'')


try:
    raiz(-1)
except Exception as err:
    print(err)





