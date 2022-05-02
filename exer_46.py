# exer_45.py

# Descrição
#   Comparação de tamanho entre Generators Expressions
#   e outras estruturas de dados preenchidas através de
#   Comprehension

# Versão 1.0

# Author: Marcus Fermino

# GitHub: https://www.github.com/mf-linux

from sys import getsizeof


l = lambda x: [n for n in range(1, x + 1)]
ge = lambda x: (n for n in range(1, x + 1))


print('Tamanhos')

print('Lista com 10 elementos: ', getsizeof(l(10)))
print('Lista com 100 elementos: ', getsizeof(l(100)))
print('Lista com 1000 elementos: ', getsizeof(l(1000)))

print('')

print('Tupla com 10 elementos: ', getsizeof(tuple(l(10))))
print('Tupla com 100 elementos: ', getsizeof(tuple(l(100))))
print('Tupla com 1000 elementos: ', getsizeof(tuple(l(1000))))

print('')

print('Conjunto com 10 elementos: ', getsizeof(set(l(10))))
print('Conjunto com 100 elementos: ', getsizeof(set(l(100))))
print('Conjunto com 1000 elementos: ', getsizeof(set(l(1000))))

print('')

print('Dicionário com 10 elementos: ', getsizeof(dict.fromkeys(l(10))))
print('Dicionário com 100 elementos: ', getsizeof(dict.fromkeys(l(100))))
print('Dicionário com 1000 elementos: ', getsizeof(dict.fromkeys(l(1000))))

print('')

print('Expressão Geradora com 10 elementos: ', getsizeof(ge(10)))
print('Expressão Geradora com 100 elementos: ', getsizeof(ge(100)))
print('Expressão Geradora com 1000 elementos: ', getsizeof(ge(1000)))
