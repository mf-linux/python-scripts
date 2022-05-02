# exer_58.py

# Descrição
#    OOP - Destrutores

# Versão 1.0

# Author: Marcus Fermino

# GitHub: https://www.github.com/mf-linux


class Pessoa:

    # Construtor é executado na criação do objeto
    def __init__(self, nome = 'Marcus'):
        self.nome = nome
        self.comprimentar()

    # Destrutor é executado na destruição do objeto
    # que ocorre através do Garbage Collector
    # quando o objeto deixa de ser necessário ou
    # ao fim do programa.
    # O destrutor também é invocado ao usar a diretiva del
    def __del__(self):
        self.despedir()

    def comprimentar(self):
        print (f'Eu sou o {self.nome} e estou vivo')
    
    def despedir(self):
        print(f'Eu sou o {self.nome} e estou morrendo')


p1 = Pessoa('José')
p2 = Pessoa()

print('')

# Mata o josé
del p1

print('\nPrograma acabando..', end='\n\n')
# O Marcus será morto ao fim do programa