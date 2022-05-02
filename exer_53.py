# exer_53.py

# Descrição
#   Encadeamento de Exceções automático

# Versão 1.0

# Author: Marcus Fermino

# GitHub: https://www.github.com/mf-linux

def raiz(x):
    if x < 0: raise ValueError


try:
    raiz(-1)
except ValueError:
    raise RuntimeError('Não realizo raízes negativas')