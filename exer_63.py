# exer_63.py

# Descrição
#   OOP - Classes abstratas

# Versão 1.0

# Author: Marcus Fermino

# GitHub: https://www.github.com/mf-linux


from abc import ABC, abstractmethod

class Poligono(ABC):

    def __str__(self) -> str:
        return '{}: {}\nLados: {}'.format(self._classificacao, self._nome, self._lados)

    @abstractmethod
    def area(self) -> float:
        pass

    @abstractmethod
    def perimetro(self) -> float:
        pass

    @property
    @abstractmethod
    def lados(self) -> tuple:
        pass

    @property
    @abstractmethod
    def classificacao(self) -> str:
        pass

    @property
    @abstractmethod
    def nome(self) -> str:
        pass

class Quadrilatero(Poligono):

    def __init__(self, lados: tuple, nome: str):
        self._nome = nome
        self._classificacao = 'Quadrilatero'
        self._lados = lados

    def perimetro(self) -> float:
        perimetro = 0
        for lado in self._lados:
            perimetro += lado
        return perimetro

    def area(self) -> float:
        return self._lados[0] * self._lados[1]
    
    @property
    def classificacao(self) -> str:
        return self._classificacao
    
    @property
    def lados(self) -> tuple:
        return self._lados
    
    @property 
    def nome(self) -> str:
        return self._nome

    @lados.setter
    def lados(self, lados: list):
        self._lados = lados

q1 = Quadrilatero((2, 4, 2, 4), 'Retangulo')
q2 = Quadrilatero((2, 2, 2, 2), 'Quadrado')


print(q1, f'Área: {q1.area()}', sep='\n')
print(q2, f'Área: {q2.area()}', sep='\n')


