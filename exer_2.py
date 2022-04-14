# exer_2.py

# Descrição
#   Exibe os tipos de dados para as variáveis em Python


# Versão 1.0

# Author: Marcus Fermino

# GitHub: https://www.github.com/mf-linux

var_i = 1                                   # Inteiro

var_f = 1.5                                 # Float

var_co = 5+2j                               # Complexo

var_s = 'Marcus Fermino'                    # String

var_b = False                               # Boolean

var_l = [var_i, var_f, var_s, var_b]        # Lista

var_t = (var_i, var_f, var_s, var_b)        # Tupla

var_d = {'inteiro': var_i,                  # Dicionário ou Hashtable ou Array Associativo
    'ponto_flutuante': var_f, 
    'complexo': var_co,
    'string': var_s,
    'booleano': var_b}

print(type(var_i))
print(type(var_f))
print(type(var_co))
print(type(var_s))
print(type(var_b))
print(type(var_l))
print(type(var_t))
print(type(var_d))

