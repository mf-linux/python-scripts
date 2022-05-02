# exer_56.py

# Descrição
#   Classes e Objetos introdução

# Versão 1.0

# Author: Marcus Fermino

# GitHub: https://www.github.com/mf-linux


# Criação da classe
class Pessoa:
    # Criação do construtor sem valores padrões
    def __init__(self, nome, idade, sexo):
        self.nome = nome
        self.idade = idade
        self.sexo = sexo

    def apresentar(self):
        return 'Meu nome: {}\nMinha Idade: {}\nMeu Sexo: {}'.format(self.nome, self.idade, self.sexo)


# Instancia o objeto
p1 = Pessoa('Gabryel', 21, 'M')
print(p1.apresentar())