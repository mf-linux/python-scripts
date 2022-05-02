# exer_62.py

# Descrição
#    OOP - Construtor para as classes filhas

# Versão 1.0

# Author: Marcus Fermino

# GitHub: https://www.github.com/mf-linux


class Pessoa:

    def __init__(self, nome='', idade=0):
        self._nome = nome
        self._idade = idade
        self._sexo = 'Não informado'

    def __init_subclass__(cls, sexo: str, **kwargs):
        cls._sexo = sexo
    
    def __str__(self) -> str:
        return '{} é do sexo {} e tem {} de idade'.format(self._nome, self._sexo, self._idade)

    @property
    def nome(self) -> str:
        return self._nome
    
    @property
    def idade(self) -> int:
        return self._idade

    @property
    def sexo(self) -> str:
        return self._sexo
    
    @nome.setter
    def nome(self, nome):
        self._nome = nome
    
    @idade.setter
    def idade(self, idade):
        self._idade = idade
    
    @sexo.setter
    def sexo(self, sexo):
        self._sexo = sexo

        
class Homem(Pessoa, sexo='M'):
    def __init__(self, nome='', idade=0):
        self.nome = nome
        self._idade = idade

class Mulher(Pessoa, sexo='F'):
    def __init__(self, nome='', idade=0):
        self.nome = nome
        self._idade = idade


m = Mulher('Wanessa', 21)
h = Homem('Marcus', 24)
p = Pessoa('José', 25)

print(m, h, p, sep='\n')




    








