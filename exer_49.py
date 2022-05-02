# exer_49.py

# Descrição
#   Múltiplos tratadores

# Versão 1.0

# Author: Marcus Fermino

# GitHub: https://www.github.com/mf-linux

try:
    a = float(input('a: '))
    b = float(input('b: '))
    r = a / b    
except ZeroDivisionError: 
    print('Impossível dividir pro zero')
except ValueError:
    print('Tipo de invalido, informe números reais')
except Exception as err:
    print('Erro:', err)
else:
    print('Sem erros')
    

