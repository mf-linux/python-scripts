# exer_56.py

# Descrição
#    OOP - Construtores parametrizados e métodos

# Versão 1.0

# Author: Marcus Fermino

# GitHub: https://www.github.com/mf-linux

import random

# Criação da classe
class Dado:
        
    # Construtor com valor padrão definido
    def __init__(self, n_lados = 6):
        self.nome = f'd{n_lados}'
        self.n_lados = n_lados
        self.l_atual = 0

    # Simula a rolagem do dado gerando um valor aleatório dentro do intervalo de 1 até o n_lados
    def rolar(self):
        self.l_atual = random.randint(1, self.n_lados)
        return self.l_atual
    
    # Permite rolar o mesmo dado n_vezes
    def rolarMult(self, n_vezes):
        r = ( self.rolar() for n in range(1, n_vezes + 1))
        return tuple(r)

    # Gera uma string contendo o nome do dado e o lado que ele parou depois de uma rolagem única
    def toString(self):
        str = '{}: {}'.format(self.nome, self.l_atual)
        return str
    


meu_d6, meu_d8, meu_d10 = Dado(), Dado(8), Dado(10)
meu_d6.rolar()
meu_d8.rolar()
meu_d10.rolar()


print(meu_d6.toString(), meu_d8.toString(), meu_d10.toString(), sep='\n')

print(f'5{meu_d6.nome}:', meu_d6.rolarMult(5))
print(f'5{meu_d8.nome}:', meu_d8.rolarMult(5))
print(f'5{meu_d10.nome}:', meu_d10.rolarMult(5))
