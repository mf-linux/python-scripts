# exer_54.py

# Descrição
#   Lançando múltiplas exceções sem encadeamento

# Versão 1.0

# Author: Marcus Fermino

# GitHub: https://www.github.com/mf-linux

def raiz(x):
    if x < 0: raise ValueError


try:
    raiz(-25)
except ValueError:
    raise RuntimeError('Não executo divisões por zero') from None
