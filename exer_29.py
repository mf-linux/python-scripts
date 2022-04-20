# exer_29.py

# Descrição
#   Trabalhando com listas

# Versão 1.0

# Author: Marcus Fermino

# GitHub: https://www.github.com/mf-linux


def mostrar(lista):
    for i in lista:
        print('%i' % lista.index(i), '%i' % lista.count(i), i, sep=' : ')
    print('(Indice', 'Número de Ocorrências', 'Valor)', sep=' : ', end='\n\n')

cores = ['Amarelo', 'Preto', 'Azul', 'Branco', 'Laranja', 'Verde', 'Vermelho']
mostrar(cores)

# Adiciona ao fim da lista
# cores.append('Roxo')
# cores.append('Roxo')
# cores.append('Roxo')
# mostrar(cores)


# Remove um item
# cores.remove('Roxo')
# mostrar(cores)

# Insere numa posição especifica
# cores.insert(0, 'Ciano')
# mostrar(cores)

# cores.insert(25, 'Magenta')
# mostrar(cores)

# cores[0] = 'Purpura'
# mostrar(cores)

# Remove de uma posicão especifica
# cores.pop(0)
# mostrar(cores)

# cores.pop(4)
# mostrar(cores)

# Ordena a lista
# cores.sort()
# mostrar(cores)

# cores.sort(reverse=True)
# mostrar(cores)

# Inverte a lista
# cores.reverse()
# mostrar(cores)

