# exer_36.py

# Descrição
#   Utilizando Conjuntos(SET)

# Versão 1.0

# Author: Marcus Fermino

# GitHub: https://www.github.com/mf-linux

def separar(valores, separador):
    temp = []
    for i in valores.split(separador):
        temp.append(i.strip())
    return temp



print('Operações com Conjuntos', end='\n\n')

a = separar(input('Informe os valores do conjunto A separados por virgula: '), ',')
a = set(a)
b = separar(input('Informe os valores do conjunto B separados por virgula: '), ',')
b = set(b)

print('\nEscolha a operação que deseja realizar', end='\n\n')
print('1 - União', '2 - Interseção', '3 - Diferença', '4 - Diferença Simétrica', sep='\n', end='\n\n')

entrada = int(input(': '))

saida = 'A {} dos conjuntos A = {} e B = {} é: C = {}'

if entrada == 1:
    # Usando operador
    saida = saida.format('união', a, b, a | b)
    # Usando método
    # saida = saida.format('união', a, b, a.union(b))                            
elif entrada == 2:
    # Usando operador
    saida = saida.format('intersecção', a, b, a & b)
    # Usando método
    # saida = saida.format('intersecção', a, b, a.intersection(b))               
elif entrada == 3:
    # Usando operador
    saida = saida.format('diferença', a, b, a - b)
    # Usando método
    # saida = saida.format('diferença', a, b, a.difference(b))                   
elif entrada == 4:
    # Usando operador
    saida = saida.format('diferença simétrica', a, b, a ^ b)
    # Usando método
    # saida = saida.format('diferença simétrica', a, b, a.symmetric_difference(b)) 
else:
    saida = 'Opção invalida'


print('\n', saida, sep='')



