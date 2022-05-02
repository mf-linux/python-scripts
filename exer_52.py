# exer_52.py

# Descrição
#   Encadeamento de Exceções manual

# Versão 1.0

# Author: Marcus Fermino

# GitHub: https://www.github.com/mf-linux


def raiz(x):
    if x < 0: raise ValueError()

try:
    raiz(-25)
except ValueError as e:
    raise RuntimeError('Erro, não calculo raízes negativas') from e