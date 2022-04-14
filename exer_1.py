# exer_1.py

# Descrição
#   Exibe ou expande o valor de variáveis


# Versão 1.0

# Author: Marcus Fermino

# GitHub: https://www.github.com/mf-linux

var_i = 1
var_s = 'Marcus'
var_f = 1.5
var_b = True


# Exibe no estilo C
print('var = %i' % var_i)
print('var = %.2f' % var_f)
print('var = %s' % var_s)
print('var = %i' % var_b)                               # 1 - True ou 0 - False

print('====')

# Exibe as variáveis usando separadores
print('var', '=', var_i)                                # Utiliza o separador padrão
print('var', var_i, sep=' = ')                          # Utiliza um separador customizado

print('====')

# Exibe usando a classe format
print('var = {}'.format(var_i))

print('====')

# Exibe as variáveis através da concatenação
print('var = ' + str(var_i))                            # Para concatenar é preciso converter os dados para string

# Exibe as variáveis por meio da expansão dentro da String
print(f'var = {var_i}')                                 # Para expandir a string deve ser precedida pelo indicador f
                                                        #   e o nome da variável deve aparecer entre {}